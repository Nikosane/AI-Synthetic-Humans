import json
from simulation.simulation import Simulation

def load_world_state():
    try:
        with open("memory/world_state.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_world_state(state):
    with open("memory/world_state.json", "w") as file:
        json.dump(state, file, indent=4)

def main():
    print("Starting AI-Generated Synthetic Humans Simulation...")
    world_state = load_world_state()
    simulation = Simulation(world_state)
    simulation.run()
    save_world_state(simulation.get_state())
    print("Simulation completed and world state saved.")

if __name__ == "__main__":
    main()
