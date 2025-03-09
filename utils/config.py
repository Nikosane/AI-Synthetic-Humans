class Config:
    WORLD_SIZE = (20, 20)
    MAX_NPCS = 50
    EVENT_PROBABILITY = 0.1
    MEMORY_FILE = "memory/npc_memory.json"

    @staticmethod
    def get_config():
        return {
            "WORLD_SIZE": Config.WORLD_SIZE,
            "MAX_NPCS": Config.MAX_NPCS,
            "EVENT_PROBABILITY": Config.EVENT_PROBABILITY,
            "MEMORY_FILE": Config.MEMORY_FILE
        }

    def __repr__(self):
        return f"Config(WORLD_SIZE={self.WORLD_SIZE}, MAX_NPCS={self.MAX_NPCS})"
