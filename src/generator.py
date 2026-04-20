import requests


class Generator:
    def __init__(self, model="llama3.2:3b-instruct-q4_K_M"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, query, context):
        prompt = f"""
You are a business analyst.

Use ONLY the provided context to answer.

IMPORTANT:
- Analyze the data carefully
- If the question involves comparison (like highest, lowest), consider all records
- Give a clear final answer

Context:
{context}

Question:
{query}

Answer:
"""

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Error: {response.status_code} - {response.text}"