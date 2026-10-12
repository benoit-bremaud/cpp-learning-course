"""Verify the four actual division excerpts without evaluating a zero divisor."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/premieres-divisions.md').read_text()
cases = dict(re.findall(r'<!-- example:division-([a-z]+) -->\s*```cpp\n(.*?)```', lesson, re.S))
assert set(cases) == {'exact', 'partial', 'insufficient', 'empty'}
source = '#include <cassert>\nint main(){\n'
for key, stock, quotient in [('exact', 12, 3), ('partial', 14, 3), ('insufficient', 3, 0), ('empty', 0, 0)]:
    lines = cases[key].strip().splitlines()
    assert len(lines) == 3
    assert lines[1] == 'int components_per_kit = 4;'
    source += '{\n'
    for index, line in enumerate(lines):
        source += line + '\n'
        source += f'assert(component_count == {stock});\n'
        if index >= 1:
            source += 'assert(components_per_kit == 4);\n'
        if index == 2:
            source += f'assert(kit_count == {quotient});\n'
    source += '}\n'
source += '}\n'
with tempfile.TemporaryDirectory(prefix='course-divisions-') as directory:
    folder = Path(directory)
    cpp = folder / 'divisions.cpp'
    binary = folder / 'divisions'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
for index, key in enumerate(['exact', 'partial', 'insufficient', 'empty'], 1):
    assert Path(f'public/diagrams/examples/division-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/first-divisions/{index:02}-activity-{key}.svg').read_bytes()
print('PASS: four C++17 division excerpts, checkpoints, preserved stock, positive divisors and SVG provenance')
