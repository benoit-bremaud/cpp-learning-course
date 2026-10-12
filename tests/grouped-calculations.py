"""Validate grouping excerpts, preserved inputs and the changed transfer contract."""
from pathlib import Path
import re
import subprocess
import tempfile

lesson = Path('src/content/docs/notions/parentheses-calculs.md').read_text()
cases = dict(re.findall(r'<!-- example:grouping-([a-z]+) -->\s*```cpp\n(.*?)```', lesson, re.S))
assert set(cases) == {'intermediate', 'grouped', 'omitted', 'outer', 'loose'}
source = '#include <cassert>\nint main(){\n'
for key, result in [('intermediate', 20), ('grouped', 20), ('omitted', 11), ('outer', 11), ('loose', 11)]:
    lines = cases[key].strip().splitlines()
    assert len(lines) == (5 if key == 'intermediate' else 4)
    inputs = [('loose_component_count', 3), ('kit_count', 2)] if key == 'loose' else [('existing_kit_count', 3), ('additional_kit_count', 2)]
    inputs.append(('components_per_kit', 4))
    source += '{\n'
    for index, line in enumerate(lines):
        source += line + '\n'
        for name, value in inputs[:min(index + 1, 3)]:
            source += f'assert({name} == {value});\n'
        if key == 'intermediate' and index >= 3:
            source += 'assert(total_kit_count == 5);\n'
        if index == len(lines) - 1:
            source += f'assert(component_count == {result});\n'
    source += '}\n'
# Confirm why the chosen inputs expose missing grouping, unlike these alternate inputs.
for key in ['grouped', 'omitted', 'outer']:
    code = cases[key]
    assert 'int existing_kit_count = 3;' in code and 'int components_per_kit = 4;' in code
    for old, new, result in [('int existing_kit_count = 3;', 'int existing_kit_count = 0;', 8),
                             ('int components_per_kit = 4;', 'int components_per_kit = 1;', 5)]:
        source += '{' + code.replace(old, new) + f'assert(component_count == {result});' + '}\n'
source += '}\n'
with tempfile.TemporaryDirectory(prefix='course-grouping-') as directory:
    folder = Path(directory)
    cpp = folder / 'grouping.cpp'
    binary = folder / 'grouping'
    cpp.write_text(source)
    subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(cpp), '-o', str(binary)], check=True)
    result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
    assert (result.returncode, result.stdout, result.stderr) == (0, '', '')
for key, stem in [('intermediate', '01-activity-intermediate'), ('grouped', '02-activity-grouped'), ('loose', '03-activity-loose')]:
    assert Path(f'public/diagrams/examples/grouping-{key}.svg').read_bytes() == Path(f'docs/architecture/diagrams/grouped-calculations/{stem}.svg').read_bytes()
print('PASS: five C++17 grouping excerpts, checkpoints, transfer/masking cases and SVG provenance')
