"""Compile actual lesson programs and verify exact output and diagram provenance."""
from pathlib import Path
import re
import subprocess
import tempfile

expected = {"ready": "Ready\n", "silent": "", "ordered": "Program started\nProgram finished\n",
            "reversed": "Program finished\nProgram started\n", "joined": "System ready\n"}
seen = set()
with tempfile.TemporaryDirectory() as directory:
    for lesson in ["programme-minimal", "premiers-affichages"]:
        text = Path(f"src/content/docs/notions/{lesson}.md").read_text()
        for key, code in re.findall(r'<!-- example:program-(\w+) -->\s*```cpp\n(.*?)```', text, re.S):
            assert key not in seen
            seen.add(key)
            source = Path(directory) / f"{key}.cpp"
            binary = Path(directory) / key
            source.write_text(code)
            subprocess.run(["g++", "-std=c++17", "-Wall", "-Wextra", "-Werror", str(source), "-o", str(binary)], check=True, capture_output=True)
            result = subprocess.run([str(binary)], capture_output=True, text=True, timeout=5)
            assert (result.returncode, result.stdout, result.stderr) == (0, expected[key], ""), key
            assert Path(f"public/diagrams/examples/program-{key}.svg").read_bytes() == Path(f"docs/architecture/diagrams/program-skeleton/{key}.svg").read_bytes()
assert seen == set(expected)
print("PASS: five C++17 lesson programs, exact output, exit status and SVG provenance")
