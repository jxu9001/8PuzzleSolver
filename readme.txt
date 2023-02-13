Jerry Xu
CS 6364 Spring 2023
Homework 1 README

INSTRUCTIONS TO RUN THE SOLVER
To run the solver, first ensure that the *.py files and the input files are in the same directory.
Next, type "python3 main.py <algorithm_name> <input_file_name>" into the terminal and press enter.
algorithm_name is one of:
    - dfs (depth first search)
    - ids (iterative deepening search)
    - astar1 (a* search with heuristic 1)
    - astar2 (a* search with heursitic 2)
input_file_name is one of:
    - input1.txt (easy, optimal solution has 5 moves)
    - input2.txt (medium, optimal solution has 9 moves)
    - input3.txt (hard, optimal solution has 12 moves)
    - input4.txt (very hard, optimal solution has 30 moves)

SAMPLE INPUT AND OUTPUTS FOR INPUT2.TXT
input2.txt represents the following initial state:
+---+---+---+
| 7 |   | 2 |
+---+---+---+
| 6 | 4 | 8 |
+---+---+---+
| 5 | 3 | 1 |
+---+---+---+
running dfs:
ERROR: Failed to find a solution at or before depth = 10

running ids:

running astar1:

running astar2:

ANALYSIS OF MY TWO HEURISTICS
Heuristic 1: # of misplaced tiles (+ moves made so far) maybe not
Heuristic 2: Σ(manhattan distance from each tile to its goal position) (+ moves made so far) maybe not

