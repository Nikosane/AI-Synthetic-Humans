class WorldObject:
    def __init__(self, name, position, interactable=True):
        self.name = name
        self.position = position
        self.interactable = interactable

    def interact(self, human):
        if self.interactable:
            return f"{human.name} interacts with {self.name}."
        return f"{self.name} is not interactable."

    def __repr__(self):
        return f"WorldObject(name={self.name}, position={self.position}, interactable={self.interactable})"
