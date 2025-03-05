import requests
import json

class BehaviorEngine:
    def __init__(self, model="deepseek-r1-1.5b"):
        self.model = model
        self.api_url = "http://localhost:11434/api/generate"

    def generate_decision(self, prompt):
        payload = {"model": self.model, "prompt": prompt, "stream": False}
        response = requests.post(self.api_url, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "No response")
        return "Error generating decision"

    def process_situation(self, human, situation):
        prompt = f"{human.name} is in a situation: {situation}. Based on their personality ({human.personality}), what should they do?"
        return self.generate_decision(prompt)

    def __repr__(self):
        return f"BehaviorEngine(model={self.model})"
