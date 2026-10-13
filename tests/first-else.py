"""Verify actual first-else programs, exact output, alternate inputs and preserved state."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/premiere-alternative.md').read_text()
entries = re.findall(r'<!-- example:first-else-([a-z-]+) -->\s*```cpp\n(.*?)```', lesson, re.S)
assert [key for key, _ in entries] == ['matched', 'below', 'above', 'identifier', 'wrong-message']
expected_original = {
    'matched': 'Target matched\nCheck finished\n',
    'below': 'Target not matched\nCheck finished\n',
    'above': 'Target not matched\nCheck finished\n',
    'identifier': 'Identifier not matched\nCheck finished\n',
    'wrong-message': 'Below target\nCheck finished\n',
}
with tempfile.TemporaryDirectory(prefix='course-first-else-') as directory:
    source, binary = Path(directory) / 'case.cpp', Path(directory) / 'case'
    for key, code in entries:
        identity = key == 'identifier'
        target = 'expected_identifier' if identity else 'measurement_target'
        value = 'observed_identifier' if identity else 'measurement_count'
        flag = 'identifier_matched' if identity else 'target_matched'
        fixed = 7 if identity else 3
        message = 'Identifier matched' if identity else 'Target matched'
        original_match = re.search(rf'int {value} = (\d+);', code)
        assert original_match
        original = int(original_match[1])
        assert original in ([5, 7, 9] if identity else [2, 3, 4])
        for count in ([5, 7, 9] if identity else [2, 3, 4]):
            variant, replacements = re.subn(rf'int {value} = \d+;', f'int {value} = {count};', code)
            assert replacements == 1
            matched = count == fixed
            negative = 'Identifier not matched' if identity else ('Below target' if key == 'wrong-message' else 'Target not matched')
            output = (message if matched else negative) + '\nCheck finished\n'
            if count == original:
                assert variant == code
                assert output == expected_original[key]
            # Instrument a separate copy; also compile and execute the unmodified teaching program.
            target_check = f'    assert({target} == {fixed});'
            inputs_check = target_check + f'\n    assert({value} == {count});'
            all_check = inputs_check + f'\n    assert({flag} == {str(matched).lower()});'
            instrumented = '#include <cassert>\n#include <type_traits>\n' + variant
            for line, checks in [
                (f'    const int {target} = {fixed};', target_check),
                (f'    int {value} = {count};', inputs_check),
                (f'    bool {flag} = {value} == {target};', all_check + f'\n    static_assert(std::is_same_v<decltype({flag}), bool>);'),
            ]:
                assert instrumented.count(line) == 1
                instrumented = instrumented.replace(line, line + '\n' + checks)
            assert instrumented.count('    return 0;') == 1
            instrumented = instrumented.replace('    return 0;', all_check + '\n    return 0;')
            for program in [variant, instrumented]:
                source.write_text(program)
                subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(source), '-o', str(binary)], check=True, capture_output=True)
                result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
                assert (result.returncode, result.stdout, result.stderr) == (0, output, ''), (key, count)
for key in ['matched', 'below', 'above', 'identifier']:
    assert Path(f'public/diagrams/examples/first-else-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/first-else/{key}.svg').read_bytes()
# Prevent divergence from approved snippets and verify the displayed output contracts.
spec = Path('docs/architecture/specs/first-else.md').read_text()
assert [code for _, code in entries] == re.findall(r'```cpp\n(.*?)```', spec, re.S)
assert re.findall(r'```text\n(.*?)```', lesson, re.S) == [expected_original[key] for key, _ in entries] + ['Target not matched\nCheck finished\n']
print('PASS: five actual C++17 programs, 15 inputs, original/instrumented state and output checks, approved sources and SVG provenance')
