"""Compile the authored counter excerpts and verify each observable checkpoint."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/mise-a-jour-compteur.md').read_text()
entries = re.findall(r'<!-- example:counter-([a-z]+) -->\s*```cpp\n(.*?)```', lesson, re.S)
cases = dict(entries)
assert len(entries) == len(cases) == 6
assert set(cases) == {'single', 'repeated', 'resumed', 'reset', 'batch', 'withdrawal'}
source = '#include <cassert>\nint main() {\n'
for key, values in [('single', [0, 1]), ('repeated', [0, 1, 2]), ('resumed', [5, 6, 7]), ('reset', [0, 1, 1])]:
    lines = cases[key].strip().splitlines()
    assert len(lines) == len(values)
    source += '{\n'
    for line, expected in zip(lines, values):
        source += line + f'\nassert(measurement_count == {expected});\n'
    if key == 'reset':
        source += 'assert(measurement_count != 2);\n'
    source += '}\n'
for key, operand, initial, quantity, final in [
    ('batch', 'added_count', 5, 3, 8),
    ('withdrawal', 'used_count', 8, 2, 6),
]:
    lines = cases[key].strip().splitlines()
    assert len(lines) == 3
    source += '{\n'
    for index, line in enumerate(lines):
        source += line + f'\nassert(component_count == {final if index == 2 else initial});\n'
        if index >= 1:
            source += f'assert({operand} == {quantity});\n'
    source += '}\n'
# Reuse the actual authored expressions for the boundary claims in the prose.
for quantity, expected in [(0, 8), (8, 0)]:
    source += '{\nint component_count = 8;\n'
    source += f'int used_count = {quantity};\n'
    source += cases['withdrawal'].strip().splitlines()[-1] + '\n'
    source += f'assert(component_count == {expected});\nassert(used_count == {quantity});\n}}\n'
# Verify the nonzero reset contrast and the comprehension question, not a copied formula.
for key, initial, expected in [('reset', 5, 1), ('repeated', 9, 11)]:
    source += f'{{\nint measurement_count = {initial};\n'
    source += '\n'.join(cases[key].strip().splitlines()[1:]) + '\n'
    source += f'assert(measurement_count == {expected});\n}}\n'
source += '}\n'
with tempfile.TemporaryDirectory(prefix='course-counter-') as directory:
    folder = Path(directory)
    cpp, binary = folder / 'counter.cpp', folder / 'counter'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
for index, key in enumerate(['single', 'repeated', 'resumed', 'batch', 'withdrawal'], 1):
    assert Path(f'public/diagrams/examples/counter-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/counter-update/{index:02}-activity-{key}.svg').read_bytes()
print('PASS: six C++17 excerpts, every checkpoint, preserved operands, boundary/contrast cases and SVG provenance')
