import subprocess
import sys

def run_flake8(file_path):
    result = subprocess.run(
        [sys.executable, "-m", "flake8", file_path],
        capture_output=True,
        text=True
    )
    return result.stdout or "No Flake8 issues found!"

def run_black_diff(file_path):
    result = subprocess.run(
        [sys.executable, "-m", "black", "--diff", file_path],
        capture_output=True,
        text=True
    )
    return result.stdout or "Code already formatted!"