"""Compile the two actual lesson excerpts and verify bytes, status and SVG provenance."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def validate_lesson(lesson: Path) -> None:
    """Reject missing/extra excerpts and verify both complete hosted C++17 contracts.

    A lesson path may point to an isolated mutation fixture. Diagram provenance
    always uses the repository paths, so fixtures cannot supply substitute assets.
    """
    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ with C++17 support is required to validate the lesson')
    text = lesson.read_text()
    blocks = re.findall(r'^```cpp[^\n]*\n(.*?)^```', text, re.M | re.S)
    marked = re.findall(r'<!-- example:program-([a-z-]+) -->\s*```cpp\n(.*?)^```', text, re.M | re.S)
    expected = {'ready': b'Ready\n', 'silent': b''}
    keys = [key for key, _code in marked]
    assert len(blocks) == 2 and len(marked) == 2, 'Expected exactly two labelled C++ fences'
    assert len(set(keys)) == 2 and set(keys) == set(expected), 'Expected unique ready and silent markers'
    assert blocks == [code for _key, code in marked], 'Every C++ fence must be labelled'
    with tempfile.TemporaryDirectory(prefix='cpp-first-program-') as directory:
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
            authoritative = Path(f'docs/architecture/diagrams/program-skeleton/{key}.svg')
            assert snapshot.read_bytes() == authoritative.read_bytes(), f'{key}: SVG provenance mismatch'
            print(f'PASS {key}: exact stdout {result.stdout!r}, empty stderr, exit 0, SVG provenance')


if __name__ == '__main__':
    validate_lesson(Path(sys.argv[1]) if len(sys.argv) > 1
                    else Path('src/content/docs/notions/programme-minimal.md'))
