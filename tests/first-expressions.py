"""Verify actual expression excerpts, their checkpoints and diagram provenance."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/premieres-expressions.mdx').read_text()
companion = Path('src/content/examples/expressions/empty-tray.md').read_text()
programs = dict(re.findall(r'\{/\* example:expression-([a-z-]+) \*/\}\s*```cpp\n(.*?)```', lesson, re.S))
programs.update(re.findall(r'<!-- example:expression-([a-z-]+) -->\s*```cpp\n(.*?)```', companion, re.S))
expected = {
    'literal': [{'component_count': 5}],
    'named': [{'left_tray_count': 2}, {'left_tray_count': 2, 'right_tray_count': 3},
              {'left_tray_count': 2, 'right_tray_count': 3, 'component_count': 5}],
    'empty-tray': [{'left_tray_count': 0}, {'left_tray_count': 0, 'right_tray_count': 3},
                   {'left_tray_count': 0, 'right_tray_count': 3, 'component_count': 3}],
    'assigned': [{'component_count': 0}, {'component_count': 5}],
}
assert set(programs) == set(expected)
source = '#include <cassert>\nint main() {\n'
for key, checkpoints in expected.items():
    actions = [line.strip() for line in programs[key].splitlines() if line.strip()]
    assert len(actions) == len(checkpoints), key
    source += '{\n'
    for action, values in zip(actions, checkpoints):
        source += action + '\n'
        source += ''.join(f'assert({name} == {value});\n' for name, value in values.items())
    source += '}\n'
# Verify the lesson's explicit claim that replacement ignores an old value of eight.
assert 'int component_count = 0;' in programs['assigned']
source += '{' + programs['assigned'].replace('int component_count = 0;', 'int component_count = 8;\nassert(component_count == 8);')
source += 'assert(component_count == 5);}\n}\n'
with tempfile.TemporaryDirectory(prefix='course-expressions-') as directory:
    folder = Path(directory)
    cpp = folder / 'expressions.cpp'
    binary = folder / 'expressions'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', ''), result
for key, stem in [('literal', '01-activity-literal'), ('named', '02-activity-named'),
                  ('empty-tray', '03-activity-empty-tray'), ('assigned', '04-activity-assigned')]:
    assert Path(f'public/diagrams/examples/expression-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/first-expressions/{stem}.svg').read_bytes(), key
print('PASS: four C++17 excerpts, all checkpoints, unchanged operands, replacement and SVG provenance')
