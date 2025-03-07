import random

class MapGenerator:
    def __init__(self, size=(10, 10)):
        self.size = size
        self.map = self.generate_map()

    def generate_map(self):
        generated_map = {}
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                generated_map[(x, y)] = random.choice(["grass", "water", "mountain", "forest"])
        return generated_map

    def display_map(self):
        for y in range(self.size[1]):
            row = " ".join(self.map[(x, y)][0].upper() for x in range(self.size[0]))
            print(row)

    def __repr__(self):
        return f"MapGenerator(size={self.size})"
