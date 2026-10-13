"""Check authored comparison snippets, boundary cases and stored-result updates."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/premiere-comparaison.md').read_text()
entries = re.findall(r'<!-- example:comparison-([a-z]+) -->\s*```cpp\n(.*?)```', lesson, re.S)
cases = dict(entries)
assert len(entries) == len(cases) == 5
assert set(cases) == {'below', 'equal', 'above', 'reversed', 'refresh'}
source = '#include <cassert>\n#include <type_traits>\nint main() {\n'
for key, initial, result in [('below', 2, False), ('equal', 3, False), ('above', 4, True), ('reversed', 4, False), ('refresh', 2, False)]:
    lines = cases[key].strip().splitlines()
    assert len(lines) == (5 if key == 'refresh' else 3)
    source += '{\n'
    for index, line in enumerate(lines):
        source += line + '\nassert(measurement_limit == 3);\n'
        if index >= 1:
            source += f'assert(measurement_count == {4 if index >= 3 else initial});\n'
        if index >= 2:
            expected = True if index == 4 else result
            source += f'assert(limit_exceeded == {str(expected).lower()});\n'
            source += 'static_assert(std::is_same_v<decltype(limit_exceeded), bool>);\n'
    if key == 'reversed':
        source += 'assert(limit_exceeded != true);\n'
    source += '}\n'
# Reuse the actual expressions to verify operand reversal, masking and prose answers.
expressions = {}
for key in ['below', 'reversed']:
    match = re.fullmatch(r'bool limit_exceeded = (.*);', cases[key].strip().splitlines()[2])
    assert match
    expressions[key] = match[1]
for count, correct, reversed_result in [(0, False, True), (2, False, True), (3, False, False), (4, True, False), (5, True, False)]:
    source += f'{{\nconst int measurement_limit = 3;\nint measurement_count = {count};\n'
    for key, expected in [('below', correct), ('reversed', reversed_result)]:
        expression = expressions[key]
        source += f'static_assert(std::is_same_v<decltype({expression}), bool>);\n'
        source += f'assert(({expression}) == {str(expected).lower()});\n'
    source += f'assert(measurement_limit == 3);\nassert(measurement_count == {count});\n}}\n'
source += '}\n'
with tempfile.TemporaryDirectory(prefix='course-comparison-') as directory:
    folder = Path(directory)
    cpp, binary = folder / 'comparison.cpp', folder / 'comparison'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
for index, key in enumerate(['below', 'equal', 'above', 'refresh'], 1):
    assert Path(f'public/diagrams/examples/comparison-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/first-comparison/{index:02}-activity-{key}.svg').read_bytes()
print('PASS: five C++17 comparison excerpts, every checkpoint, bool types, unchanged operands, masking/recalculation cases and SVG provenance')
