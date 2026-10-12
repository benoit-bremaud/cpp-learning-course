"""Verify the exact valid/rejected pair authored in CPP-01."""
from pathlib import Path
import os
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/cpp-01.mdx').read_text()
programs = dict(re.findall(r'\{/\* example:(assignment-[a-z]+) \*/\}\s*```cpp\n(.*?)```', lesson, re.S))
assert set(programs) == {'assignment-valid', 'assignment-rejected'}
with tempfile.TemporaryDirectory() as directory:
    folder = Path(directory)
    valid = folder / 'valid.cpp'
    valid.write_text(programs['assignment-valid'])
    binary = folder / 'valid'
    # The teaching program intentionally does not observe the assigned value.
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', '-Wno-unused-but-set-variable', str(valid), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
    instrumented = '#include <cassert>\n' + programs['assignment-valid'].replace('int measurement_count = 0;', 'int measurement_count = 0;\nassert(measurement_count == 0);').replace('    measurement_count = 1;', '    measurement_count = 1;\nassert(measurement_count == 1);')
    valid.write_text(instrumented)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(valid), '-o', str(binary)], check=True)
    subprocess.run([str(binary)], check=True, timeout=5)
    rejected = folder / 'rejected.cpp'
    rejected.write_text(programs['assignment-rejected'])
    result = subprocess.run(['g++', '-std=c++17', '-fsyntax-only', str(rejected)], capture_output=True, text=True, env={**os.environ, 'LC_ALL': 'C'})
    assert result.returncode != 0
    assert "error: redeclaration of 'int measurement_count'" in result.stderr, result.stderr
assert Path('public/diagrams/examples/assignment-main.svg').read_bytes() == Path('docs/architecture/diagrams/value-comparisons/04-activity-assignment-main.svg').read_bytes()
print('PASS: complete assignment program, checkpoints, intended redeclaration diagnostic and SVG provenance')
