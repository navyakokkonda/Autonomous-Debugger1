# ai_engine.py
# MOCK MODE — No OpenAI Required

def generate_patch(context_files, error_output):
    """
    Mock AI patch generator.
    Simulates fixing a simple assertion bug.
    """

    for file, content in context_files.items():
        if "assert 1 + 1 == 3" in content:
            return f"""--- {file}
+++ {file}
@@
-    assert 1 + 1 == 3
+    assert 1 + 1 == 2
"""

    return ""