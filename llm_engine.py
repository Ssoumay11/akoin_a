import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "llama-3.3-70b-versatile"


def generate_response(context, user_query):

    prompt = f"""
You are a regulatory reporting assistant for PRA COREP C01.00 (Own Funds).

Use ONLY the regulatory context provided.
If information is missing, state that clearly.

Context:
{context}

User Question:
{user_query}

If the question includes a monetary amount, use that amount as the "value".


Respond strictly in JSON format:
{{
  "template": "C01.00",
  "fields": [
    {{
      "row_code": "",
      "field_name": "",
      "value": "",
      "justification": ""
    }}
  ]
}}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=600,
    )

    return response.choices[0].message.content
