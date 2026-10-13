"""Check actual strict/inclusive snippets, checkpoints and masked substitutions."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/atteindre-ou-depasser.md').read_text()
entries = re.findall(r'<!-- example:inclusive-([a-z-]+) -->\s*```cpp\n(.*?)```', lesson, re.S)
cases = dict(entries)
expected = {
    'below': (2, False, False),
    'equal': (3, False, True),
    'above': (4, True, True),
    'strict-for-inclusive': (3, False, False),
    'inclusive-for-strict': (3, True, True),
}
assert len(entries) == len(cases) == 5
assert set(cases) == set(expected)
source = '#include <cassert>\n#include <type_traits>\nint main() {\n'
for key, (count, strict, inclusive) in expected.items():
    lines = cases[key].strip().splitlines()
    assert len(lines) == 4
    source += '{\n'
    for index, line in enumerate(lines):
        source += line + '\nassert(measurement_limit == 3);\n'
        if index >= 1:
            source += f'assert(measurement_count == {count});\n'
        if index >= 2:
            source += f'assert(limit_exceeded == {str(strict).lower()});\n'
            source += 'static_assert(std::is_same_v<decltype(limit_exceeded), bool>);\n'
        if index >= 3:
            source += f'assert(limit_reached == {str(inclusive).lower()});\n'
            source += 'static_assert(std::is_same_v<decltype(limit_reached), bool>);\n'
    if key == 'strict-for-inclusive':
        source += 'assert(limit_reached != true);\n'
    if key == 'inclusive-for-strict':
        source += 'assert(limit_exceeded != false);\n'
    source += '}\n'
# Reuse all three authored versions with the three boundary-neighborhood inputs.
for key in ['equal', 'strict-for-inclusive', 'inclusive-for-strict']:
    expressions = []
    for line in cases[key].strip().splitlines()[2:]:
        match = re.fullmatch(r'bool (limit_exceeded|limit_reached) = (.*);', line)
        assert match
        expressions.append(match[2])
    for count in [2, 3, 4]:
        answers = {2: (False, False), 3: expected[key][1:], 4: (True, True)}[count]
        source += f'{{\nconst int measurement_limit = 3;\nint measurement_count = {count};\n'
        for expression, answer in zip(expressions, answers):
            source += f'static_assert(std::is_same_v<decltype({expression}), bool>);\n'
            source += f'assert(({expression}) == {str(answer).lower()});\n'
        source += f'assert(measurement_limit == 3);\nassert(measurement_count == {count});\n}}\n'
source += '}\n'
with tempfile.TemporaryDirectory(prefix='course-inclusive-') as directory:
    folder = Path(directory)
    cpp, binary = folder / 'inclusive.cpp', folder / 'inclusive'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
for index, key in enumerate(['below', 'equal', 'above'], 1):
    assert Path(f'public/diagrams/examples/inclusive-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/inclusive-comparison/{index:02}-activity-{key}.svg').read_bytes()
print('PASS: five C++17 excerpts, every checkpoint, bool types, unchanged inputs, both substitutions and masking cases, SVG provenance')
