"""Check actual multiplication excerpts and data that expose or mask a wrong operator."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/premieres-multiplications.md').read_text()
cases = dict(re.findall(r'<!-- example:multiplication-([a-z]+) -->\s*```cpp\n(.*?)```', lesson, re.S))
assert set(cases) == {'literal', 'named', 'one', 'zero', 'wrong'}
source = '#include <cassert>\nint main() {\n'
for name, kits, expected in [('literal', None, 12), ('named', 3, 12), ('one', 1, 4), ('zero', 0, 0), ('wrong', 3, 7)]:
    lines = cases[name].strip().splitlines()
    assert len(lines) == (1 if kits is None else 3)
    source += '{\n'
    for index, line in enumerate(lines):
        source += line + '\n'
        if kits is not None:
            source += f'assert(kit_count == {kits});\n'
            if index >= 1:
                source += 'assert(components_per_kit == 4);\n'
        if index == len(lines) - 1:
            source += f'assert(component_count == {expected});\n'
    source += '}\n'
# Use the actual expressions from both snippets to verify the table, not retyped formulas.
for name in ['named', 'wrong']:
    code = cases[name]
    assert 'int kit_count = 3;' in code and 'int components_per_kit = 4;' in code
    code = code.replace('int kit_count = 3;', 'int kit_count = 2;').replace('int components_per_kit = 4;', 'int components_per_kit = 2;')
    source += '{' + code + 'assert(component_count == 4);}\n'
source += '}\n'
with tempfile.TemporaryDirectory(prefix='course-multiplications-') as directory:
    folder = Path(directory)
    cpp = folder / 'multiplications.cpp'
    binary = folder / 'multiplications'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
for key, stem in [('literal', '01-activity-literal'), ('named', '02-activity-named'), ('zero', '03-activity-zero'), ('one', '04-activity-one')]:
    assert Path(f'public/diagrams/examples/multiplication-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/first-multiplications/{stem}.svg').read_bytes()
print('PASS: five C++17 snippets, checkpoints, unchanged inputs, discriminating/masking data and SVG provenance')
