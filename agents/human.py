import json

class Human:
    def __init__(self, name, age, personality):
        self.name = name
        self.age = age
        self.personality = personality
        self.memory = []

    def remember(self, event):
        self.memory.append(event)
        with open(f"memory/{self.name}_memory.json", "w") as file:
            json.dump(self.memory, file, indent=4)

    def decide_action(self, situation):
        return f"{self.name} reacts to {situation} based on personality: {self.personality}"

    def __repr__(self):
        return f"Human(name={self.name}, age={self.age}, personality={self.personality})"
