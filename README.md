﻿# Local-Search-Algorithms

This repository implements a **Hill Climbing algorithm** for an agent navigating a 2D environment. The simulation includes an interactive visualization built with **Pygame**, where an agent optimizes its position on a map based on a specified metric.

---

## Demo

https://github.com/user-attachments/assets/abfb1f8a-1f2d-48a9-8940-ccd28a7dd88a


---

## Installation
1. Clone this repository:
   ```bash
   cd
   git clone https://github.com/Loki-Silvres/Local-Search-Algorithms.git
   cd Local-Search-Algorithms
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the simulation:
   ```bash
   cd src
   python hill_climbing.py
   ```

---

## File Structure
- **`main.py`**: Entry point for the simulation.
- **`map.py`**: Defines the 2D map and its associated metrics.
- **`agent.py`**: Implements the agent's behavior and actions.
- **`local_search_algorithms.py`**: Contains the Hill Climbing algorithm implementation.
- **`config.py`**: Centralized configuration settings (e.g., screen size, colors, FPS).

---

## Key Components
1. **Agent**: 
   - Tracks its current position and state.
   - Uses the Hill Climbing algorithm to evaluate the best possible action.
2. **Map**:
   - Defines the environment and metrics for optimization.
   - Visualizes the agent and terrain.
3. **Local Search Algorithm**:
   - Evaluates possible actions and selects the one with the best metric value.

---

## Configuration
Modify `config.py` to adjust simulation parameters such as:
- **Window dimensions**: `WINDOW_WIDTH`, `WINDOW_HEIGHT`
- **Colors**: `WHITE`, `BLACK`, etc.
- **Frames per second**: `FPS`
- **Agent step size**: `AGENT_STEP`


---

## Future Improvements
- Add support for more complex search algorithms (e.g., Simulated Annealing, Genetic Algorithms).
- Expand the map with dynamic obstacles.
- Include multiple agents for competitive/cooperative tasks.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

---

## Contact
If you have any questions or suggestions, feel free to reach out:
- **Email**: [alok9360@gmail.com](alok9360@gmail.com)
- **GitHub**: [GitHub](https://github.com/Loki-Silvres) 

---
