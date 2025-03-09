import json

class Helpers:
    @staticmethod
    def load_json(file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_json(file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def __repr__(self):
        return "Helpers Module"
