"""Verify actual first-if programs, exact output, alternate inputs and preserved state."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/premiere-condition.md').read_text()
entries = re.findall(r'<!-- example:first-if-([a-z]+) -->\s*```cpp\n(.*?)```', lesson, re.S)
assert [key for key, _ in entries] == ['matched', 'unmatched', 'identifier', 'misplaced']
expected_original = {
    'matched': 'Target matched\nCheck finished\n',
    'unmatched': 'Check finished\n',
    'identifier': 'Identifier matched\nCheck finished\n',
    'misplaced': '',
}
with tempfile.TemporaryDirectory(prefix='course-first-if-') as directory:
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
            output = (message + '\n' if matched else '') + ('Check finished\n' if matched or key != 'misplaced' else '')
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
for index, key in enumerate(['matched', 'unmatched', 'identifier'], 1):
    assert Path(f'public/diagrams/examples/first-if-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/first-if/{index:02}-activity-{key}.svg').read_bytes()
print('PASS: four actual C++17 programs, 12 input configurations, exact stdout/status, instrumented state checks, misplaced continuation and SVG provenance')
