import requests

class LLMHandler:
    def __init__(self, model_endpoint="http://localhost:11434/api/generate"):
        self.model_endpoint = model_endpoint

    def query_model(self, prompt):
        payload = {"model": "deepseek-r1-1.5b", "prompt": prompt, "max_tokens": 256}
        response = requests.post(self.model_endpoint, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "")
        return "Error: Unable to get response from LLM"

    def __repr__(self):
        return f"LLMHandler(model_endpoint={self.model_endpoint})"
