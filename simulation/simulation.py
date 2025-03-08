from agents.human import Human
from world.world import World
from world.environment import Environment

class Simulation:
    def __init__(self):
        self.world = World()
        self.environment = Environment()
        self.npcs = []

    def add_npc(self, npc):
        self.npcs.append(npc)

    def run_step(self):
        self.environment.update_conditions()
        for npc in self.npcs:
            npc.decide_action()
        print("Simulation step executed.")

    def run(self, steps=10):
        for _ in range(steps):
            self.run_step()

    def __repr__(self):
        return f"Simulation(npcs={len(self.npcs)})"
