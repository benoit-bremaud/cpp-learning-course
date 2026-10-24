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
    marked = re.findall(r'<!-- example:program-([a-z-]+) -->\s*```cpp(?: wrap)?\n(.*?)^```', text, re.M | re.S)
    keys = [key for key, _code in marked]
    count = len(expected)
    count_label = 'two' if count == 2 else 'three'
    assert len(blocks) == count and len(marked) == count, f'Expected exactly {count_label} labelled C++ fences'
    assert len(set(keys)) == count and set(keys) == set(expected), ('Expected unique ready and silent markers'
        if count == 2 else 'Expected unique ordered, reversed and joined markers')
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
            snapshot = Path(f'public/diagrams/examples/program-{key}.svg')
            authoritative = models[key]
            assert snapshot.read_bytes() == authoritative.read_bytes(), f'{key}: SVG provenance mismatch'
            print(f'PASS {key}: exact stdout {result.stdout!r}, empty stderr, exit 0, SVG provenance')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path, help='Isolated lesson mutation fixture')
    parser.add_argument('--lesson', choices=['first-program', 'ordered-output'], default='first-program')
    args = parser.parse_args()
    if args.lesson == 'first-program':
        validate_lesson(args.path or Path('src/content/docs/notions/programme-minimal.md'))
    else:
        _validate_programs(args.path or Path('src/content/docs/notions/premiers-affichages.md'), {
            'ordered': b'Program started\nProgram finished\n',
            'reversed': b'Program finished\nProgram started\n',
            'joined': b'System ready\n',
        }, {
            key: Path(f'docs/architecture/diagrams/ordered-output/{number}-activity-{key}.svg')
            for number, key in [('01', 'ordered'), ('02', 'reversed'), ('03', 'joined')]
        })
