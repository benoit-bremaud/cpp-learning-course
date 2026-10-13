"""Verify authored less-than examples, traces, equivalent relations and UML snapshots."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/en-dessous-ou-au-maximum.md').read_text()
entries = re.findall(r'<!-- example:lower-([a-z]+) -->\s*```cpp\n(.*?)```', lesson, re.S)
assert [key for key, _ in entries] == ['below', 'equal', 'above', 'capacity', 'reversed']
cases = dict(entries)
expected = {'below': (2, True, True), 'equal': (3, False, True),
            'above': (4, False, False), 'capacity': (8, False, True),
            'reversed': (2, False, True)}
source = '#include <cassert>\n#include <type_traits>\nint main() {\n'
for key, code in entries:
    capacity = key == 'capacity'
    names = ['box_capacity', 'item_count', 'has_space', 'within_capacity'] if capacity else ['measurement_limit', 'measurement_count', 'below_limit', 'within_limit']
    values = [8 if capacity else 3, *expected[key]]
    lines = code.strip().splitlines()
    assert len(lines) == 4
    source += '{\n'
    for index, line in enumerate(lines):
        source += line + '\n'
        for checkpoint in range(index + 1):
            source += f'assert({names[checkpoint]} == {str(values[checkpoint]).lower()});\n'
        if index >= 2:
            source += f'static_assert(std::is_same_v<decltype({names[index]}), bool>);\n'
    source += '}\n'
# Exercise the actual authored expressions with values that expose and mask errors.
for key, counts in [('below', [0, 2, 3, 4, 20]), ('reversed', [0, 2, 3, 4, 20]), ('capacity', [7, 8, 9])]:
    capacity = key == 'capacity'
    limit, value, maximum = ('box_capacity', 'item_count', 8) if capacity else ('measurement_limit', 'measurement_count', 3)
    for count in counts:
        source += f'{{const int {limit} = {maximum}; int {value} = {count};\n'
        answers = [maximum < count if key == 'reversed' else count < maximum, count <= maximum]
        for line, answer in zip(cases[key].strip().splitlines()[2:], answers):
            match = re.fullmatch(r'bool (\w+) = (.*);', line)
            assert match
            name, expression = match.groups()
            source += line + f'\nassert({name} == {str(answer).lower()});\n'
            source += f'static_assert(std::is_same_v<decltype({expression}), bool>);\n'
        source += f'assert({limit} == {maximum}); assert({value} == {count});\n'
        if not capacity:
            source += 'assert((measurement_count < measurement_limit) == (measurement_limit > measurement_count));\n'
        source += '}\n'
source += '}\n'
with tempfile.TemporaryDirectory(prefix='course-lower-') as directory:
    cpp = Path(directory) / 'lower.cpp'
    binary = Path(directory) / 'lower'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
for index, key in enumerate(['below', 'equal', 'above', 'capacity'], 1):
    assert Path(f'public/diagrams/examples/lower-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/lower-comparisons/{index:02}-activity-{key}.svg').read_bytes()
print('PASS: five C++17 snippets, every checkpoint, bool types, unchanged inputs, reversed and equivalent relations, capacity cases and SVG provenance')
