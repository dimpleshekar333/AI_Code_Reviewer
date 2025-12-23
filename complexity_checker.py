import subprocess
import sys

def run_radon(file_path):
    result = subprocess.run(
        [sys.executable, "-m", "radon", "cc", file_path, "-a"],
        capture_output=True,
        text=True
    )
    return result.stdout