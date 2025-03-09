from llm_api.llm_handler import LLMHandler

class DecisionMaker:
    def __init__(self):
        self.llm = LLMHandler()

    def make_decision(self, situation):
        prompt = f"Given the situation: '{situation}', what should the NPC do?"
        return self.llm.query_model(prompt)

    def __repr__(self):
        return "DecisionMaker using Deepseek R1 1.5B"
