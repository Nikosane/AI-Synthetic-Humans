import random

class EventSystem:
    def __init__(self):
        self.events = ["earthquake", "flood", "disease outbreak", "festival", "trade fair"]

    def generate_event(self):
        return random.choice(self.events)

    def trigger_event(self):
        event = self.generate_event()
        print(f"Event triggered: {event}")
        return event

    def __repr__(self):
        return f"EventSystem(events={self.events})"
