"""Compile actual guarded-update examples and verify outputs and pre/post state."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/ajout-sous-limite.md').read_text()
entries = re.findall(r'<!-- example:guarded-([a-z-]+) -->\s*```cpp\n(.*?)```', lesson, re.S)
assert [key for key, _ in entries] == ['room', 'full', 'box', 'inclusive-error', 'already-above']
spec = dict(re.findall(r'### ([a-z-]+)\n\n```cpp\n(.*?)```', Path('docs/architecture/specs/guarded-increment.md').read_text(), re.S))
assert re.findall(r'```text\n(.*?)```', lesson, re.S) == ['Count increased\n3\n', 'Addition refused\n3\n', 'Count increased\n8\n', 'Count increased\n4\n', 'Addition refused\n3\n', 'Addition refused\n4\n']
with tempfile.TemporaryDirectory(prefix='guarded-count-') as tmp:
    source, binary = Path(tmp)/'sample.cpp', Path(tmp)/'sample'
    for key, code in entries:
        assert code == spec[key]
        box = key == 'box'
        count = 'item_count' if box else 'measurement_count'
        limit = 'box_capacity' if box else 'measurement_limit'
        maximum = 8 if box else 3
        for initial in [0, maximum-1, maximum, maximum+1, 20]:
            allowed = initial <= maximum if key == 'inclusive-error' else initial < maximum
            final = initial + int(allowed)
            variant, replacements = re.subn(rf'int {count} = \d+;', f'int {count} = {initial};', code)
            assert replacements == 1
            expected = ('Count increased' if allowed else 'Addition refused') + f'\n{final}\n'
            instrumented = '#include <cassert>\n#include <type_traits>\n' + variant
            point = re.search(r'    bool can_add = .*?;', instrumented)[0]
            pre = f'\n    assert({count} == {initial});\n    assert({limit} == {maximum});\n    assert(can_add == {str(allowed).lower()});\n    static_assert(std::is_same_v<decltype(can_add), bool>);'
            instrumented = instrumented.replace(point, point + pre)
            post = f'    assert({count} == {final});\n    assert({limit} == {maximum});\n    assert(can_add == {str(allowed).lower()});\n'
            instrumented = instrumented.replace('    return 0;', post + '    return 0;')
            for program in [variant, instrumented]:
                source.write_text(program)
                subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(source), '-o', str(binary)], check=True, capture_output=True)
                result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
                assert (result.returncode, result.stdout, result.stderr) == (0, expected, ''), (key, initial)
for key in ['room', 'full', 'box', 'already-above']:
    authoritative = next(Path('docs/architecture/diagrams/guarded-increment').glob(f'*-{key}.svg'))
    assert authoritative.read_bytes() == Path(f'public/diagrams/examples/guarded-{key}.svg').read_bytes()
print('PASS: five approved programs, 25 inputs, 50 plain/instrumented runs, exact output, pre/post state and SVG provenance')
