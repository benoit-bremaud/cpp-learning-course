"""Check the actual CPP-09 excerpts, including the intended compile rejection."""
from pathlib import Path
import os
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/cpp-09.md').read_text()
def excerpt(label):
    matches = re.findall(r'<!-- example:' + re.escape(label) + r' -->\s*```cpp\n(.*?)```', lesson, re.S)
    assert len(matches) == 1, label
    return matches[0]

env = dict(os.environ, LC_ALL='C')
with tempfile.TemporaryDirectory(prefix='constant-limit-') as folder:
    root = Path(folder)
    def compile_case(name, body, syntax_only=False):
        source = root / (name + '.cpp')
        source.write_text('#include <cassert>\nint main() {\n' + body + '\n}\n')
        command = ['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror']
        command += ['-fsyntax-only', str(source)] if syntax_only else [str(source), '-o', str(root / name)]
        return subprocess.run(command, capture_output=True, text=True, env=env)

    actions = [line.strip() for line in excerpt('constant-valid').splitlines() if line.strip()]
    assert len(actions) == 3, 'Review checkpoints when the primary excerpt changes'
    checks = ['assert(measurement_limit == 3);', 'assert(measurement_limit == 3 && measurement_count == 0);', 'assert(measurement_limit == 3 && measurement_count == 1);']
    valid = compile_case('valid', '\n'.join(action + check for action, check in zip(actions, checks)))
    assert valid.returncode == 0, valid.stderr
    subprocess.run([str(root / 'valid')], check=True)
    invalid = compile_case('rejected', excerpt('constant-rejected'), syntax_only=True)
    assert invalid.returncode != 0
    assert "assignment of read-only variable 'measurement_limit'" in invalid.stderr, invalid.stderr
    wrong = compile_case('wrong', excerpt('constant-wrong-value') + '\nassert(measurement_limit == 30); assert(measurement_limit != 3);')
    assert wrong.returncode == 0, wrong.stderr
    subprocess.run([str(root / 'wrong')], check=True)
print('PASS: constant checkpoints, intended GCC rejection, and wrong-but-valid initial value')
