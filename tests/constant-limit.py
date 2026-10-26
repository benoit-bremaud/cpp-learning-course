"""Validate CPP-09's actual complete sources, compiler rejection and SVG provenance."""
from pathlib import Path
import argparse
import re
import shutil
import subprocess
import tempfile


def _compile(source: Path, binary: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', '-pedantic-errors',
         str(source), '-o', str(binary)], capture_output=True, timeout=30, check=False)


def _execute(binary: Path, expected: bytes, label: str) -> None:
    result = subprocess.run([str(binary)], stdin=subprocess.DEVNULL,
                            capture_output=True, timeout=5, check=False)
    assert result.stdout == expected, f'{label}: unexpected stdout: {result.stdout!r}'
    assert result.stderr == b'', f'{label}: unexpected stderr: {result.stderr!r}'
    assert result.returncode == 0, f'{label}: unexpected exit status: {result.returncode}'


def _statements(code: str) -> list[str]:
    body = re.fullmatch(r'\s*#include <iostream>\s+int main\(\)\s*\{([^{}]*)\}\s*', code)
    assert body, 'Expected one complete iostream/main source without helpers'
    return re.sub(r'\s+', '', body[1]).split(';')


def validate_lesson(lesson: Path) -> None:
    """Check a fixed three-source contract, never executing the rejected translation unit.

    Alternate paths support isolated mutations. Expected bytes, source intent and
    authoritative diagram paths always come from this harness, never the fixture.
    Two independently successful controls isolate the forbidden const assignment.
    """
    assert shutil.which('g++'), 'g++ with C++17 support is required'
    text = lesson.read_text()
    blocks = re.findall(r'^```cpp[^\n]*\n(.*?)^```', text, re.M | re.S)
    marked = re.findall(r'<!-- example:program-([a-z-]+) -->\s*```cpp wrap\n(.*?)^```', text, re.M | re.S)
    assert len(blocks) == 3 and len(marked) == 3, 'Expected exactly three labelled complete sources'
    expected_keys = ['constant-stable', 'constant-rejected', 'constant-wrong']
    assert [key for key, _ in marked] == expected_keys, 'Expected unique stable/rejected/wrong markers in lesson order'
    assert blocks == [code for _, code in marked], 'Every C++ fence must be labelled'
    sources = dict(marked)
    expected = {'constant-stable': b'3\n0\n3\n1\n', 'constant-wrong': b'30\n0\n30\n1\n'}
    observation = ['std::cout<<measurement_limit', 'std::cout<<"\\n"',
                   'std::cout<<measurement_count', 'std::cout<<"\\n"']
    with tempfile.TemporaryDirectory(prefix='cpp-constants-') as directory:
        folder = Path(directory)
        for key, output in expected.items():
            source = folder / f'{key}.cpp'
            binary = folder / key
            source.write_text(sources[key])
            build = _compile(source, binary)
            assert build.returncode == 0, f'{key}: C++17 compilation failed: {build.stderr.decode()}'
            _execute(binary, output, key)
            limit = 3 if key == 'constant-stable' else 30
            assert _statements(sources[key]) == [
                f'constintmeasurement_limit={limit}', 'intmeasurement_count=0',
                *observation, 'measurement_count=1', *observation, 'return0', '',
            ], f'{key}: expected twelve const/variable-observation statements'
            print(f'PASS {key}: exact stdout, empty stderr, exit 0')
        rejected = sources['constant-rejected']
        source = folder / 'constant-rejected.cpp'
        source.write_text(rejected)
        build = _compile(source, folder / 'never-run')
        assert build.returncode != 0, 'constant-rejected: expected compilation rejection'
        # Never execute a binary for the ill-formed source, even if a compiler left one.
        for name, control, output in [
            ('mutable', rejected.replace('const int measurement_limit', 'int measurement_limit'), b'4\n'),
            ('removed-assignment', rejected.replace('    measurement_limit = 4;\n', ''), b'3\n'),
        ]:
            source = folder / f'{name}.cpp'
            source.write_text(control)
            binary = folder / name
            build = _compile(source, binary)
            assert build.returncode == 0, f'{name}: rejection control must compile: {build.stderr.decode()}'
            _execute(binary, output, name)
        assert _statements(rejected) == [
            'constintmeasurement_limit=3', 'measurement_limit=4',
            'std::cout<<measurement_limit', 'std::cout<<"\\n"', 'return0', '',
        ], 'constant-rejected: expected five statements isolating const assignment'
        print('PASS constant-rejected: compile-only rejection and both successful controls')
    for asset, model in [('constant-limit', 'stable-limit'), ('constant-wrong-limit', 'wrong-limit')]:
        assert Path(f'public/diagrams/examples/{asset}.svg').read_bytes() == Path(
            f'docs/architecture/diagrams/observable-constants/07-activity-{model}.svg').read_bytes(), 'SVG provenance mismatch'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('lesson', nargs='?', type=Path, default=Path('src/content/docs/notions/cpp-09.md'))
    validate_lesson(parser.parse_args().lesson)
