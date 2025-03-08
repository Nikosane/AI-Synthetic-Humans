class Interaction:
    def __init__(self, npc1, npc2):
        self.npc1 = npc1
        self.npc2 = npc2

    def engage(self):
        if self.npc1.personality.traits["sociability"] > 0.5:
            return f"{self.npc1.name} greets {self.npc2.name}."
        return f"{self.npc1.name} ignores {self.npc2.name}."

    def __repr__(self):
        return f"Interaction({self.npc1.name}, {self.npc2.name})"
