"""Compile authored C++17 excerpts and verify observations, including negative controls."""
from pathlib import Path
import re
import subprocess
import tempfile
import resource

resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def blocks(path):
    return re.findall(r'```cpp[^\n]*\n(.*?)```', Path(path).read_text(), re.S)


def checkpoints(code, variable, values):
    actions = [line.strip() for line in code.splitlines() if line.strip()]
    assert len(actions) == len(values)
    return ''.join(action + f'assert({variable} == {value});' for action, value in zip(actions, values))


stock = blocks('src/content/examples/variables/component-stock.md')[0]
copy = blocks('src/content/examples/variables/independent-copy.md')[0]
reservoir = blocks('src/content/examples/conditions/reservoir-level.md')[0]
strict, inclusive = blocks('src/content/examples/conditions/inclusive-threshold.md')
guided, = blocks('src/content/docs/exemple-voyant.mdx')
valid_const, rejected_const, wrong_const = blocks('src/content/docs/notions/cpp-09.md')
# Compare executable tokens: the pinned reference includes an explanatory comment.
assert re.sub(r'//[^\n]*|\s+', '', strict) == re.sub(r'//[^\n]*|\s+', '', guided)
source = '#include <cassert>\n#include <initializer_list>\n' + reservoir + strict + inclusive
source += '\nint main() {\n'
source += '{' + checkpoints(stock, 'component_count', [12, 11]) + '}\n'
source += '{' + copy.replace('int snapshot_count', 'assert(component_count == 12); int snapshot_count').replace('component_count = 11;', 'assert(snapshot_count == 12); component_count = 11;') + 'assert(component_count == 11 && snapshot_count == 12);}\n'
source += '{' + valid_const + 'assert(measurement_limit == 3 && measurement_count == 1);}\n'
source += '{' + wrong_const + 'assert(measurement_limit == 30 && measurement_limit != 3);}\n'
source += '''
for (int level : {0, 19}) assert(should_warn_low_level(level));
for (int level : {20, 21, 100}) assert(!should_warn_low_level(level));
for (int temperature : {29, 30, 31}) {
    assert(should_light_indicator(temperature) == (temperature == 31));
    assert(should_light_indicator_inclusive(temperature) == (temperature >= 30));
}
}
'''
with tempfile.TemporaryDirectory(prefix='course-excerpts-') as folder:
    path = Path(folder)
    program = path / 'examples.cpp'
    program.write_text(source)
    command = ['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(program), '-o', str(path / 'examples')]
    subprocess.run(command, check=True)
    subprocess.run([str(path / 'examples')], check=True)
    # A changed boundary must be caught by the same observations, not just compile.
    program.write_text(source.replace('temperature_celsius > threshold_celsius', 'temperature_celsius >= threshold_celsius'))
    subprocess.run(command, check=True)
    result = subprocess.run([str(path / 'examples')], capture_output=True)
    assert result.returncode != 0, 'Boundary mutation escaped the assertions'
    program.write_text('int main() {' + rejected_const + '}')
    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode != 0 and 'measurement_limit' in result.stderr
print('PASS: all nine remaining excerpts, intermediate values, boundary mutation and rejected const assignment')
