"""Check actual subtraction snippets, including the valid-but-wrong formula."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/premieres-soustractions.md').read_text()
cases = dict(re.findall(r'<!-- example:subtraction-([a-z]+) -->\s*```cpp\n(.*?)```', lesson, re.S))
assert set(cases) == {'literal', 'named', 'empty', 'reversed'}
source = '#include <cassert>\nint main() {\n'
for name, expected, used in [('literal', 7, None), ('named', 7, 5), ('empty', 0, 12), ('reversed', -7, 5)]:
    lines = cases[name].strip().splitlines()
    assert len(lines) == (1 if used is None else 3)
    source += '{\n'
    for index, line in enumerate(lines):
        source += line + '\n'
        if used is not None:
            source += 'assert(initial_count == 12);\n'
            if index >= 1:
                source += f'assert(used_count == {used});\n'
        if index == len(lines) - 1:
            source += f'assert(remaining_count == {expected});\n'
            if name == 'reversed':
                source += 'assert(remaining_count != 7);\n'
    source += '}\n'
source += '}\n'
with tempfile.TemporaryDirectory(prefix='course-subtractions-') as directory:
    folder = Path(directory)
    cpp = folder / 'subtractions.cpp'
    binary = folder / 'subtractions'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
for key, stem in [('literal', '01-activity-literal'), ('named', '02-activity-named'), ('empty', '03-activity-empty')]:
    assert Path(f'public/diagrams/examples/subtraction-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/first-subtractions/{stem}.svg').read_bytes()
print('PASS: four C++17 subtraction snippets, checkpoints, unchanged inputs, wrong-but-valid result and SVG provenance')
