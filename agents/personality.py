import random

class Personality:
    def __init__(self, traits=None):
        self.traits = traits if traits else self.generate_random_traits()

    def generate_random_traits(self):
        return {
            "aggressiveness": random.uniform(0, 1),
            "kindness": random.uniform(0, 1),
            "curiosity": random.uniform(0, 1),
            "sociability": random.uniform(0, 1)
        }

    def modify_trait(self, trait, value):
        if trait in self.traits:
            self.traits[trait] = max(0, min(1, self.traits[trait] + value))

    def __repr__(self):
        return f"Personality(traits={self.traits})"
