import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_fix(code, error_output):
    prompt = f"""
You are an AI debugging agent.
The following Python code has a bug:

{code}

It fails with this output:

{error_output}

Please return a corrected version of the code that fixes the bug.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content