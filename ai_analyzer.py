import ollama

def analyze_incident(issue):

    prompt = f"""
You are an experienced SRE engineer.

Issue:
{issue}

Provide:
1. Probable Root Cause
2. Recommended Resolution
3. Confidence Score (%)

Keep the response concise.
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]