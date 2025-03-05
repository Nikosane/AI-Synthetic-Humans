import json

class Memory:
    def __init__(self, human_name):
        self.file_path = f"memory/{human_name}_memory.json"
        self.memory = self.load_memory()

    def load_memory(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def store_memory(self, event):
        self.memory.append(event)
        with open(self.file_path, "w") as file:
            json.dump(self.memory, file, indent=4)

    def recall_memories(self):
        return self.memory

    def __repr__(self):
        return f"Memory(file_path={self.file_path})"
