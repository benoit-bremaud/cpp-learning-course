"""Compile the actual teaching excerpts and check their approved contracts locally."""
from pathlib import Path
import re
import subprocess
import tempfile

root = Path('src/content/examples')
def excerpts(name):
    return re.findall(r'```cpp\n(.*?)```', next(root.rglob(name + '.md')).read_text(), re.S)

stock = excerpts('component-stock')[0]
copy = excerpts('independent-copy')[0]
reservoir = excerpts('reservoir-level')[0]
strict, inclusive = excerpts('inclusive-threshold')
source = '#include <cassert>\n' + reservoir + strict + inclusive + '\nint main() {\n'
lesson = Path('src/content/docs/notions/cpp-01.mdx').read_text()
measurement = dict(re.findall(r'\{/\* example:(measurement-[a-z]+) \*/\}\s*```cpp\n(.*?)```', lesson, re.S))
assert set(measurement) == {'measurement-primary', 'measurement-repeated'}
for name, checkpoints in [('measurement-primary', [0, 1]), ('measurement-repeated', [0, 1, 1])]:
    actions = [line.strip() for line in measurement[name].splitlines() if line.strip()]
    assert len(actions) == len(checkpoints), name
    source += '{' + ''.join(action + f'assert(measurement_count == {value});' for action, value in zip(actions, checkpoints)) + '}\n'
assert Path('public/diagrams/examples/repeated-assignment.svg').read_bytes() == Path('docs/architecture/diagrams/value-comparisons/01-activity-repeat.svg').read_bytes()
source += '{' + stock + 'assert(component_count == 11); }\n'
source += '{' + copy + 'assert(component_count == 11); assert(snapshot_count == 12); }\n'
source += """
for (int level : {0, 19}) assert(should_warn_low_level(level));
for (int level : {20, 21, 100}) assert(!should_warn_low_level(level));
assert(!should_light_indicator(29));
assert(!should_light_indicator(30));
assert(should_light_indicator(31));
assert(!should_light_indicator_inclusive(29));
assert(should_light_indicator_inclusive(30));
assert(should_light_indicator_inclusive(31));
}
"""
source = '#include <initializer_list>\n' + source
with tempfile.TemporaryDirectory(prefix='course-excerpts-') as folder:
    path = Path(folder)
    (path / 'examples.cpp').write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(path / 'examples.cpp'), '-o', str(path / 'examples')], check=True)
    subprocess.run([str(path / 'examples')], check=True)
print('PASS: actual C++17 excerpts satisfy the teaching contracts, including all five measurement checkpoints')
