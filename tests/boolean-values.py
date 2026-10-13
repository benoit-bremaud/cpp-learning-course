"""Validate the actual boolean lesson excerpts, types, traces and model snapshots."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/premiers-booleens.md').read_text()
entries = re.findall(r'<!-- example:boolean-([a-z]+) -->\s*```cpp\n(.*?)```', lesson, re.S)
cases = dict(entries)
assert len(entries) == len(cases) == 6
expected = {
    'absent': [(False, None)],
    'present': [(True, None)],
    'changes': [(False, None), (True, None), (False, None)],
    'copy': [(False, None), (False, False), (True, False)],
    'refresh': [(False, None), (False, False), (True, False), (True, True)],
    'wrong': [(True, None)],
}
assert set(cases) == set(expected)
source = '#include <cassert>\n#include <type_traits>\nint main() {\n'
for key, checkpoints in expected.items():
    lines = cases[key].strip().splitlines()
    assert len(lines) == len(checkpoints)
    source += '{\n'
    for line, (current, snapshot) in zip(lines, checkpoints):
        source += line + '\n'
        source += 'static_assert(std::is_same_v<decltype(fault_present), bool>);\n'
        source += f'assert(fault_present == {str(current).lower()});\n'
        if snapshot is not None:
            source += 'static_assert(std::is_same_v<decltype(fault_snapshot), bool>);\n'
            source += f'assert(fault_snapshot == {str(snapshot).lower()});\n'
    if key == 'wrong':
        source += 'assert(fault_present != false);\n'
    source += '}\n'
source += '}\n'
with tempfile.TemporaryDirectory(prefix='course-booleans-') as directory:
    folder = Path(directory)
    cpp, binary = folder / 'booleans.cpp', folder / 'booleans'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
for index, key in enumerate(['absent', 'present', 'changes', 'copy', 'refresh'], 1):
    assert Path(f'public/diagrams/examples/boolean-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/boolean-values/{index:02}-activity-{key}.svg').read_bytes()
print('PASS: six C++17 boolean excerpts, types, every checkpoint, independent/refreshed copy, wrong requirement and SVG provenance')
