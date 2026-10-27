"""Compile actual lesson excerpts and verify bytes, status and SVG provenance."""
from pathlib import Path
import re
import shutil
import subprocess
import argparse
import tempfile


def validate_lesson(lesson: Path) -> None:
    """Reject missing/extra excerpts and verify both complete hosted C++17 contracts.

    A lesson path may point to an isolated mutation fixture. Diagram provenance
    always uses the repository paths, so fixtures cannot supply substitute assets.
    """
    _validate_programs(lesson, {'ready': b'Ready\n', 'silent': b''}, {
        key: Path(f'docs/architecture/diagrams/program-skeleton/{key}.svg')
        for key in ['ready', 'silent']
    })


def _validate_programs(lesson: Path, expected: dict[str, bytes], models: dict[str, Path]) -> None:
    # Fixed contracts stay separate from extraction so a fixture cannot redefine success.
    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ with C++17 support is required to validate the lesson')
    text = lesson.read_text()
    blocks = re.findall(r'^```cpp[^\n]*\n(.*?)^```', text, re.M | re.S)
    marked = re.findall(r'(?:<!--|\{/\*) example:program-([a-z-]+) (?:-->|\*/\})\s*```cpp(?: wrap)?\n(.*?)^```', text, re.M | re.S)
    keys = [key for key, _code in marked]
    count = len(expected)
    count_label = {1: 'one', 2: 'two', 3: 'three'}[count]
    assert len(blocks) == count and len(marked) == count, f'Expected exactly {count_label} labelled C++ fences'
    expected_keys = list(expected)
    marker_label = (expected_keys[0] if count == 1 else
                    ', '.join(expected_keys[:-1]) + ' and ' + expected_keys[-1])
    marker_suffix = 'marker' if count == 1 else 'markers'
    assert len(set(keys)) == count and set(keys) == set(expected), f'Expected unique {marker_label} {marker_suffix}'
    assert blocks == [code for _key, code in marked], 'Every C++ fence must be labelled'
    with tempfile.TemporaryDirectory(prefix='cpp-program-output-') as directory:
        for key, code in marked:
            source = Path(directory) / f'{key}.cpp'
            binary = Path(directory) / key
            source.write_text(code)
            build = subprocess.run(
                [compiler, '-std=c++17', '-Wall', '-Wextra', '-Werror', '-pedantic-errors',
                 str(source), '-o', str(binary)],
                capture_output=True, timeout=30, check=False)
            assert build.returncode == 0, f'{key}: C++17 compilation failed: {build.stderr.decode()}'
            result = subprocess.run([str(binary)], stdin=subprocess.DEVNULL,
                                    capture_output=True, timeout=5, check=False)
            assert result.stdout == expected[key], f'{key}: unexpected stdout: {result.stdout!r}'
            assert result.stderr == b'', f'{key}: unexpected stderr: {result.stderr!r}'
            assert result.returncode == 0, f'{key}: unexpected exit status: {result.returncode}'
            if key == 'measurement-observed':
                # Output alone cannot prove that the learner reads the variable twice.
                body = re.search(r'int main\(\)\s*\{(.*?)\}', code, re.S)
                statements = re.sub(r'\s+', '', body[1]).split(';') if body else []
                assert statements == [
                    'intmeasurement_count=0', 'std::cout<<measurement_count',
                    'std::cout<<"\\n"', 'measurement_count=1',
                    'std::cout<<measurement_count', 'std::cout<<"\\n"', 'return0', '',
                ], 'measurement-observed: expected seven variable-observation statements'
            if key in ['arithmetic-update', 'literal-replacement']:
                # The literal 3 can match one output without expressing the old-value dependency.
                body = re.fullmatch(r'\s*#include <iostream>\s+int main\(\)\s*\{([^{}]*)\}\s*', code)
                assert body, f'{key}: expected one complete iostream/main source'
                statements = re.sub(r'\s+', '', body[1]).split(';')
                assignment = ('measurement_count=measurement_count+1' if key == 'arithmetic-update'
                              else 'measurement_count=1')
                assert statements == [
                    'intmeasurement_count=2', 'std::cout<<measurement_count',
                    'std::cout<<"\\n"', assignment,
                    'std::cout<<measurement_count', 'std::cout<<"\\n"', 'return0', '',
                ], f'{key}: expected seven arithmetic/replacement observation statements'
            snapshot = Path('public/diagrams/examples/measurement-count.svg' if key == 'measurement-observed'
                            else f'public/diagrams/examples/program-{key}.svg')
            authoritative = models[key]
            assert snapshot.read_bytes() == authoritative.read_bytes(), f'{key}: SVG provenance mismatch'
            print(f'PASS {key}: exact stdout {result.stdout!r}, empty stderr, exit 0, SVG provenance')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path, help='Isolated lesson mutation fixture')
    parser.add_argument('--lesson', choices=['first-program', 'ordered-output', 'observable-variables', 'arithmetic-update'], default='first-program')
    args = parser.parse_args()
    if args.lesson == 'first-program':
        validate_lesson(args.path or Path('src/content/docs/notions/programme-minimal.md'))
    elif args.lesson == 'arithmetic-update':
        _validate_programs(args.path or Path('src/content/docs/notions/premiers-calculs.md'), {
            'arithmetic-update': b'2\n3\n',
            'literal-replacement': b'2\n1\n',
        }, {
            key: Path(f'docs/architecture/diagrams/arithmetic-update/07-activity-{key}.svg')
            for key in ['arithmetic-update', 'literal-replacement']
        })
    elif args.lesson == 'observable-variables':
        _validate_programs(args.path or Path('src/content/docs/notions/cpp-01.mdx'), {
            'measurement-observed': b'0\n1\n',
        }, {
            'measurement-observed': Path('docs/architecture/diagrams/measurement-count/02-activity-observed-values.svg'),
        })
    else:
        _validate_programs(args.path or Path('src/content/docs/notions/premiers-affichages.md'), {
            'ordered': b'Program started\nProgram finished\n',
            'reversed': b'Program finished\nProgram started\n',
            'joined': b'System ready\n',
        }, {
            key: Path(f'docs/architecture/diagrams/ordered-output/{number}-activity-{key}.svg')
            for number, key in [('01', 'ordered'), ('02', 'reversed'), ('03', 'joined')]
        })
