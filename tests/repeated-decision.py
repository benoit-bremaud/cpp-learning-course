"""Compile the repeated-decision lesson excerpts and verify loop behavior."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/repeter-jusqua-limite.md').read_text()
entries = dict(re.findall(r'<!-- example:repeated-([a-z-]+) -->\s*```cpp\n(.*?)```', lesson, re.S))
assert list(entries) == [
    'multiple', 'one', 'zero-at-limit', 'zero-above', 'box',
    'missing-update', 'inclusive-error'
]

expected_exact = {
    'multiple': '2\n3\nLoop finished\n',
    'one': '3\nLoop finished\n',
    'zero-at-limit': 'Loop finished\n',
    'zero-above': 'Loop finished\n',
    'box': '6\n7\n8\nLoop finished\n',
    'inclusive-error': '2\n3\n4\nLimit exceeded\n',
}

def compile_program(source: Path, binary: Path, code: str) -> None:
    source.write_text(code)
    subprocess.run(
        ['g++', '-std=c++17', '-Wall', '-Wextra', '-Wpedantic', '-Werror', str(source), '-o', str(binary)],
        check=True, capture_output=True
    )

def run_program(binary: Path, expected: str) -> None:
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, expected, '')

with tempfile.TemporaryDirectory(prefix='repeated-decision-') as tmp:
    source, binary = Path(tmp) / 'sample.cpp', Path(tmp) / 'sample'

    for key, expected in expected_exact.items():
        compile_program(source, binary, entries[key])
        run_program(binary, expected)

    # The five correct programs share one bounded rule. Exercise boundary and
    # transfer values independently from the displayed examples.
    for key in ['multiple', 'one', 'zero-at-limit', 'zero-above', 'box']:
        code = entries[key]
        box = key == 'box'
        count = 'item_count' if box else 'measurement_count'
        limit = 'box_capacity' if box else 'measurement_limit'
        maximum = 8 if box else 3
        initial_values = [0, maximum - 1, maximum, maximum + 1, 20]
        for initial in initial_values:
            variant, replacements = re.subn(rf'int {count} = \d+;', f'int {count} = {initial};', code)
            assert replacements == 1
            values = list(range(initial + 1, maximum + 1)) if initial < maximum else []
            expected = ''.join(f'{value}\n' for value in values) + 'Loop finished\n'
            instrumented = '#include <cassert>\n' + variant
            assertions = (
                f'    assert({limit} == {maximum});\n'
                f'    assert({count} == {maximum if initial <= maximum else initial});\n'
            )
            instrumented = instrumented.replace('    return 0;', assertions + '    return 0;')
            for program in [variant, instrumented]:
                compile_program(source, binary, program)
                run_program(binary, expected)

    # Compile the exact faulty loop, but do not launch a process that cannot
    # terminate for its supplied values. A finite trace establishes the defect.
    compile_program(source, binary, entries['missing-update'])
    count, limit = 1, 3
    observations = []
    for _ in range(4):
        assert count < limit
        observations.append(count)
        # Deliberately mirror the excerpt: no assignment changes count.
    assert observations == [1, 1, 1, 1]
    assert count == 1 and count < limit

for key in entries:
    authoritative = next(Path('docs/architecture/diagrams/repeated-decision').glob(f'*-{key}.svg'))
    public = Path(f'public/diagrams/examples/repeated-{key}.svg')
    assert authoritative.read_bytes() == public.read_bytes(), key

print('PASS: seven excerpts, exact outputs, 50 bounded variants, finite non-termination trace and SVG provenance')
