Jerry Xu
CS 6364 Spring 2023
Homework 1 README

INSTRUCTIONS TO RUN THE SOLVER
To run the solver, first ensure that the *.py files and the input files are in the same directory.
Next, type "python3 main.py <algorithm_name> <input_file_name>" into the terminal and press enter.
algorithm_name is one of:
    dfs (depth first search)
    bfs (breadth first search (this wasn't required, but I implemented it to calculate the # of moves in the optimal solutions))
    ids (iterative deepening search)
    astar1 (a* search with heuristic 1)
    astar2 (a* search with heuristic 2)
input_file_name is one of:
    input1.txt (easy, optimal solution has 5 moves)
    input2.txt (medium, optimal solution has 9 moves)
    input3.txt (hard, optimal solution has 12 moves)
    input4.txt (very hard, optimal solution has 30 moves)

SAMPLE INPUT AND OUTPUTS FOR INPUT2.TXT
input2.txt represents the following initial state:
    +---+---+---+
    | 7 |   | 2 |
    +---+---+---+
    | 6 | 4 | 8 |
    +---+---+---+
    | 5 | 3 | 1 |
    +---+---+---+
output of "python3 main.py dfs input2.txt":
    ERROR: Failed to find a solution at or before depth = 10

output of "python3 main.py ids input2.txt":
    Input (Any random position of the tiles):

    7 * 2
    6 4 8
    5 3 1

    Output (List of states starting from input to goal state, if found):

    7 * 2 (Initial input state)
    6 4 8
    5 3 1

    7 2 *
    6 4 8
    5 3 1

    7 2 8
    6 4 *
    5 3 1

    7 2 8
    6 4 1
    5 3 *

    7 2 8
    6 4 1
    5 * 3

    7 2 8
    6 * 1
    5 4 3

    7 * 8
    6 2 1
    5 4 3

    7 8 *
    6 2 1
    5 4 3

    7 8 1
    6 2 *
    5 4 3

    7 8 1 (Goal state)
    6 * 2
    5 4 3

    Number of moves = 9
    Number of states enqueued = 943

    Note: * represents an empty tile

output of "python3 main.py astar1 input2.txt":
    Input (Any random position of the tiles):

    7 * 2
    6 4 8
    5 3 1

    Output (List of states starting from input to goal state, if found):

    7 * 2 (Initial input state)
    6 4 8
    5 3 1

    7 2 *
    6 4 8
    5 3 1

    7 2 8
    6 4 *
    5 3 1

    7 2 8
    6 4 1
    5 3 *

    7 2 8
    6 4 1
    5 * 3

    7 2 8
    6 * 1
    5 4 3

    7 * 8
    6 2 1
    5 4 3

    7 8 *
    6 2 1
    5 4 3

    7 8 1
    6 2 *
    5 4 3

    7 8 1 (Goal state)
    6 * 2
    5 4 3

    Number of moves = 9
    Number of states enqueued = 57

    Note: * represents an empty tile

output of "python3 main.py astar2 input2.txt":
    Input (Any random position of the tiles):

    7 * 2
    6 4 8
    5 3 1

    Output (List of states starting from input to goal state, if found):

    7 * 2 (Initial input state)
    6 4 8
    5 3 1

    7 2 *
    6 4 8
    5 3 1

    7 2 8
    6 4 *
    5 3 1

    7 2 8
    6 4 1
    5 3 *

    7 2 8
    6 4 1
    5 * 3

    7 2 8
    6 * 1
    5 4 3

    7 * 8
    6 2 1
    5 4 3

    7 8 *
    6 2 1
    5 4 3

    7 8 1
    6 2 *
    5 4 3

    7 8 1 (Goal state)
    6 * 2
    5 4 3

    Number of moves = 9
    Number of states enqueued = 27

    Note: * represents an empty tile

ANALYSIS OF MY TWO HEURISTICS
I used the two heuristics discussed in the lecture slides.
Heuristic 1: # of misplaced tiles
Heuristic 2: Σ(manhattan distance from each tile to its goal position)
