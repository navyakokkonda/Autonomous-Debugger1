# auto_debugger_ai.py

from test_runner import run_tests
from failure_parser import parse_failure
from context_builder import load_related_files
from ai_engine import generate_patch
from patch_utils import apply_patch, backup_file, restore_backup, hash_patch

from git import Repo
import time

MAX_ATTEMPTS = 5


def commit_changes():
    repo = Repo(".")
    repo.git.add(A=True)
    repo.index.commit("AI: Autonomous bug fix")


def autonomous_debug():
    seen_patches = set()

    for attempt in range(1, MAX_ATTEMPTS + 1):

        print(f"\n=== Attempt {attempt} ===")
        status, output = run_tests()

        if status == 0:
            print("All tests passed 🎉")
            commit_changes()
            return

        failing_file = parse_failure(output)

        if not failing_file:
            print("Could not detect failing file.")
            return

        print(f"Detected failing file: {failing_file}")

        backup_file(failing_file)

        context_files = load_related_files(failing_file)

        patch = generate_patch(context_files, output)

        patch_hash = hash_patch(patch)

        if patch_hash in seen_patches:
            print("Repeated patch detected. Stopping.")
            return

        seen_patches.add(patch_hash)

        success = apply_patch(patch)

        if not success:
            print("Patch failed. Restoring backup.")
            restore_backup(failing_file)
            return

        print("Patch applied. Re-testing...")
        time.sleep(1)

    print("Max attempts reached.")


if __name__ == "__main__":
    autonomous_debug()