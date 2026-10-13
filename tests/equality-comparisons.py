"""Check actual equality excerpts, unchanged inputs, masking cases and UML provenance."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/egal-ou-different.md').read_text()
entries = re.findall(r'<!-- example:equality-([a-z]+) -->\s*```cpp\n(.*?)```', lesson, re.S)
assert [key for key, _ in entries] == ['equal', 'below', 'above', 'identifier', 'threshold']
cases = dict(entries)
expected = {'equal': (3, True, False), 'below': (2, False, True),
            'above': (4, False, True), 'identifier': (9, False, True),
            'threshold': (4, True, True)}
source = '#include <cassert>\n#include <type_traits>\nint main() {\n'
for key, code in entries:
    identity = key == 'identifier'
    names = ['expected_identifier', 'observed_identifier', 'identifier_matched', 'identifier_different'] if identity else ['measurement_target', 'measurement_count', 'target_matched', 'target_different']
    values = [7 if identity else 3, *expected[key]]
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
# Reuse the actual authored expressions for both sides of equality and the faulty threshold.
for key, counts in [('equal', [0, 2, 3, 4, 20]), ('threshold', [0, 2, 3, 4, 20]), ('identifier', [5, 7, 9])]:
    identity = key == 'identifier'
    target, value, expected_value = ('expected_identifier', 'observed_identifier', 7) if identity else ('measurement_target', 'measurement_count', 3)
    for count in counts:
        source += f'{{const int {target} = {expected_value}; int {value} = {count};\n'
        answers = [count >= expected_value if key == 'threshold' else count == expected_value, count != expected_value]
        for line, answer in zip(cases[key].strip().splitlines()[2:], answers):
            match = re.fullmatch(r'bool (\w+) = (.*);', line)
            assert match
            name, expression = match.groups()
            source += line + f'\nassert({name} == {str(answer).lower()});\n'
            source += f'static_assert(std::is_same_v<decltype({expression}), bool>);\n'
        source += f'assert({target} == {expected_value}); assert({value} == {count});\n'
        source += '}\n'
source += '}\n'
with tempfile.TemporaryDirectory(prefix='course-equality-') as directory:
    cpp = Path(directory) / 'equality.cpp'
    binary = Path(directory) / 'equality'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
for index, key in enumerate(['equal', 'below', 'above', 'identifier'], 1):
    assert Path(f'public/diagrams/examples/equality-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/equality-comparisons/{index:02}-activity-{key}.svg').read_bytes()
print('PASS: five C++17 excerpts, all checkpoints, bool types, unchanged inputs, exact matching, threshold masking/exposure and SVG provenance')
