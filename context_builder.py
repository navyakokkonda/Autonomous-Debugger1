# context_builder.py

import ast
import os

def extract_imports(code):
    """
    Extract imported module names from Python code
    """
    tree = ast.parse(code)
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                imports.append(n.name.split(".")[0])

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module.split(".")[0])

    return list(set(imports))


def load_related_files(base_file):
    """
    Load failing file + its imported local modules
    """
    with open(base_file, "r") as f:
        base_code = f.read()

    related_files = {base_file: base_code}

    imports = extract_imports(base_code)

    for imp in imports:
        possible_file = imp + ".py"
        if os.path.exists(possible_file):
            with open(possible_file, "r") as f:
                related_files[possible_file] = f.read()

    return related_files