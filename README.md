# TSP on GNN
A Graph Neural Network-based Guided Local Search system for solving the Travelling Salesman Problem on a real map of Greece.

This application:
- Generates a TSP graph from real Greek city locations  
- Trains a Graph Neural Network to predict **regret values** for edges  
- Builds a route using Guided Local Search with 3 optimization algorithms  
- Displays results on an interactive folium map in a PyQt5 GUI

---

## Features
- Graphical UI with map of Greece
- Add cities manually or auto-generate 5, 10, 20, or 50 random cities
- Take this cities lat and lng and their names from excel dataset
- Trainable GNN model for regret prediction
- Guided Local Search with:
  - Greedy Nearest Neighbor (using regret, not distance)  
  - Relocate algorithm  
  - 2-opt local search on penalized edges  
- Compares GNN+GLS result vs classical TSP solver
- Visualization of the final best path

---


## Requirements

### UI
<img width="1916" height="1037" alt="MainWindow" src="https://github.com/user-attachments/assets/75572a2f-e783-46e0-9973-ec85c5b4f3fe" />

### After The Selection Of The Cities
<img width="865" height="854" alt="Click" src="https://github.com/user-attachments/assets/6059a6eb-3a59-4623-9354-455fcfaa8dfc" />
