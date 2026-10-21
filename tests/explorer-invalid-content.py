"""Check build rejection in an isolated copy without editing the working tree."""
from pathlib import Path
import shutil
import subprocess
import tempfile

root = Path.cwd()
with tempfile.TemporaryDirectory(prefix='course-invalid-') as folder:
    target = Path(folder)
    for name in ['src', 'public']:
        shutil.copytree(root / name, target / name)
    for name in ['package.json', 'package-lock.json', 'astro.config.mjs', 'tsconfig.json']:
        shutil.copy2(root / name, target / name)
    # Astro resolves component caches by physical path; use independent dependencies.
    shutil.copytree(root / 'node_modules', target / 'node_modules', symlinks=True, ignore=shutil.ignore_patterns('.vite', '.astro'))
    scenarios = [
        ('src/content/examples/variables/independent-copy.md', 'id: independent-copy', 'id: component-stock', 'Duplicate example id'),
        ('src/content/examples/variables/component-stock.md', 'category: other-contexts', 'category: invalid-category', 'category'),
        ('src/content/examples/variables/component-stock.md', 'prerequisites: [notions/cpp-01]', 'prerequisites: [missing-page]', 'Unknown prerequisite'),
        ('src/content/docs/notions/cpp-01.mdx', 'examples: [component-stock, independent-copy]', 'examples: [missing-example, independent-copy]', 'Unknown example'),
        ('src/content/docs/notions/cpp-01.mdx', 'examples: [component-stock, independent-copy]', 'examples: [component-stock, component-stock]', 'Duplicate example reference'),
        ('src/content/docs/notions/cpp-01.mdx', 'examples: [component-stock, independent-copy]', 'examples: [component-stock]', 'Empty example category'),
    ]
    for filename, before, after, expected in scenarios:
        path = target / filename
        original = path.read_text()
        assert before in original
        path.write_text(original.replace(before, after))
        result = subprocess.run(['npm', 'run', 'build'], cwd=target, capture_output=True, text=True)
        path.write_text(original)
        output = result.stdout + result.stderr
        assert result.returncode != 0 and expected in output, output[-4000:]
        print('PASS: build rejects ' + expected, flush=True)
