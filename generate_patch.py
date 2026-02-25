def generate_patch(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    prompt = f"""
    The following Python code has a bug. Fix it so that all tests pass:
    ```python
    {code}
    ```
    Return only the corrected code.
    """

    # Call GPT API (once you set your API key)
    corrected_code = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    ).choices[0].message.content

    with open(file_path, "w") as f:
        f.write(corrected_code)