import random

class World:
    def __init__(self, size=(10, 10)):
        self.size = size
        self.grid = self.generate_world()

    def generate_world(self):
        world = {}
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                world[(x, y)] = 0 if random.random() > 0.1 else 1  # 1 represents an obstacle
        return world

    def display_world(self):
        for y in range(self.size[1]):
            row = "".join("#" if self.grid[(x, y)] == 1 else "." for x in range(self.size[0]))
            print(row)

    def __repr__(self):
        return f"World(size={self.size})"
