# patch_utils.py

import subprocess
import hashlib
import shutil
import os


def backup_file(file):
    if not os.path.exists(file + ".backup"):
        shutil.copy(file, file + ".backup")


def restore_backup(file):
    if os.path.exists(file + ".backup"):
        shutil.copy(file + ".backup", file)


def apply_patch(patch_text):
    with open("ai_fix.patch", "w") as f:
        f.write(patch_text)

    result = subprocess.run(
        ["git", "apply", "ai_fix.patch"],
        capture_output=True,
        text=True
    )

    return result.returncode == 0


def hash_patch(patch):
    return hashlib.md5(patch.encode()).hexdigest()