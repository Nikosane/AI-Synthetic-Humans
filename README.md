# AI-Generated Synthetic Humans for Simulations

## Overview
This project creates AI-generated NPCs (synthetic humans) that operate within a simulated world, learning human-like movement, conversations, and decision-making. NPCs will have distinct personalities, memories, and goals, evolving through AI-driven interactions. The project leverages Deepseek R1 1.5B via Ollama for decision-making and reinforcement learning for adaptive behaviors.

## Features
- **AI-Powered NPCs**: Unique personalities, learning capabilities, and decision-making.
- **Realistic Movement**: Pathfinding with A* algorithm or reinforcement learning.
- **Procedural World Generation**: Dynamic environment with interactive objects.
- **Persistent AI Memory**: NPCs remember interactions and evolve over time.
- **Emergent Behaviors**: AI-driven interactions that lead to unpredictable results.
- **Event System**: Random and AI-triggered world events.

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Nikosane/AI_Synthetic_Humans.git
   cd AI_Synthetic_Humans
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the simulation:**
   ```sh
   python main.py
   ```

## Dependencies
- Python 3.8+
- Deepseek R1 1.5B via Ollama
- NumPy, Pandas
- Pygame (for visualization, optional)
- NetworkX (for pathfinding algorithms)

## Future Enhancements
- Implement reinforcement learning for adaptive AI behaviors.
- Add voice synthesis for realistic NPC speech.
- Expand world complexity with dynamic weather and economy simulation.
