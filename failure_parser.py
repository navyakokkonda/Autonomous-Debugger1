# failure_parser.py

import re

def parse_failure(output):
    """
    Extract first relevant Python file from pytest failure output.
    """
    matches = re.findall(r"([A-Za-z0-9_\/\\]+\.py):\d+", output)

    for m in matches:
        if "site-packages" not in m:
            return m

    return None