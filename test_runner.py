# test_runner.py

import subprocess

def run_tests():
    """
    Runs pytest and returns (status_code, full_output)
    """
    result = subprocess.run(
        ["pytest", "-q", "--tb=short"],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    return result.returncode, result.stdout + result.stderr