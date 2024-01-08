# Bushfire-Simulation
A simulator of the bushfire spreading across a forest is created. The forest is represented as a square two-dimensional grid where each cell can be in one of three states:
•	'F': A healthy tree
•	'T': A tree on fire
•	'E': An empty space (either because it was always empty, or a tree was there but it burned down)

At each time step in the simulation, the state of the forest changes according to these rules:
•	A healthy tree ('F') will catch fire ('T') if at least one of its neighbors (up, down, left, or right) is on fire.
•	A tree on fire ('T') will burn down and become an empty space ('E').
•	An empty space ('E') remains an empty space as there is nothing to burn.

The simulation ends when there are no more trees on fire. The steps it takes to finish a simulation is counted and how many healthy trees are left (if any).
To create a simulation, the following tasks are completed:
1.	Create a forest of a given size and density. Density is a number between 0 and 1 indicating a ratio of healthy trees to the overall size of the forest. For example, density = 0.4 means that 40% of cells are occupied by trees and the remaining 60% are empty.
2.	Start the fire on a randomly selected tree and spread the fire on one step taking the current state of the forest and return updated state following rules above.
3.	Run the bushfire in the created forest by spreading it one step at a time and counting the number of steps for the fire to stop, that is, the length of the bushfire.
4.	Run 1000 simulations of the bushfire, that is repeat above steps 1000 times, and provide an average length of the bushfire and number of healthy trees to survive.

