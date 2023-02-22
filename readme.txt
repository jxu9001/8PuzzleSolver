Jerry Xu
CS 6364 Spring 2023
Homework 1 README

*** INSTRUCTIONS TO RUN THE SOLVER ***
1. Ensure that the *.py files and the input files are in the same directory.
2. Type "python3 main.py <algorithm_name> <input_file_name>" into the terminal
3. Press enter
algorithm_name is one of:
    dfs (depth first search)
    bfs (breadth first search (not required, but useful to calculate the # of moves in the optimal solutions))
    ids (iterative deepening search)
    astar1 (a* search with heuristic 1)
    astar2 (a* search with heuristic 2)
input_file_name is one of:
    input1.txt (easy, optimal solution has 5 moves)
    input1.txt (medium, optimal solution has 9 moves)
    input3.txt (hard, optimal solution has 12 moves)
    input4.txt (very hard, optimal solution has 30 moves)

*** SAMPLE INPUT AND OUTPUTS FOR input1.txt ***
input1.txt represents the following initial state:
    +---+---+---+
    | 6 | 7 | 1 |
    +---+---+---+
    | 8 | 2 |   |
    +---+---+---+
    | 5 | 4 | 3 |
    +---+---+---+

output of "python3 main.py dfs input1.txt":
    ERROR: Failed to find a solution at or before depth = 10

output of "python3 main.py ids input1.txt":
    Input (Any random position of the tiles):

    6 7 1
    8 2 *
    5 4 3

    Output (List of states starting from input to goal state, if found):

    6 7 1 (Initial input state)
    8 2 *
    5 4 3

    6 7 1
    8 * 2
    5 4 3

    6 7 1
    * 8 2
    5 4 3

    * 7 1
    6 8 2
    5 4 3

    7 * 1
    6 8 2
    5 4 3

    7 8 1 (Goal state)
    6 * 2
    5 4 3

    Number of moves = 5
    Number of states enqueued = 99

    Note: * represents an empty tile

output of "python3 main.py astar1 input1.txt":
    Input (Any random position of the tiles):

    6 7 1
    8 2 *
    5 4 3

    Output (List of states starting from input to goal state, if found):

    6 7 1 (Initial input state)
    8 2 *
    5 4 3

    6 7 1
    8 * 2
    5 4 3

    6 7 1
    * 8 2
    5 4 3

    * 7 1
    6 8 2
    5 4 3

    7 * 1
    6 8 2
    5 4 3

    7 8 1 (Goal state)
    6 * 2
    5 4 3

    Number of moves = 5
    Number of states enqueued = 14

    Note: * represents an empty tile

output of "python3 main.py astar2 input1.txt":
    Input (Any random position of the tiles):

    6 7 1
    8 2 *
    5 4 3

    Output (List of states starting from input to goal state, if found):

    6 7 1 (Initial input state)
    8 2 *
    5 4 3

    6 7 1
    8 * 2
    5 4 3

    6 7 1
    * 8 2
    5 4 3

    * 7 1
    6 8 2
    5 4 3

    7 * 1
    6 8 2
    5 4 3

    7 8 1 (Goal state)
    6 * 2
    5 4 3

    Number of moves = 5
    Number of states enqueued = 12

    Note: * represents an empty tile

*** ANALYSIS OF MY TWO HEURISTICS ***
I used the two heuristics discussed in the lecture slides.
    h1: total # of misplaced tiles
    h2: Σ(manhattan distance from each tile to its goal position)

h1 assumes that it takes one move to move a misplaced tile to its correct position, and h2 does not account for the
non-empty tiles between the misplaced tile and its correct position. Both h1 and h2 underestimate the number of moves
needed to move a misplaced tile to its correct position and are therefore admissible.

A heuristic h(n) is consistent if h(n) <= path_cost(n, n') + h(n'). In this problem, the path_cost is 1 because state n'
is generated from state n by swapping the empty tile with an adjacent tile. Thus, consistency requires that
h(n) - h(n') <= 1. If we swap the empty tile with an adjacent tile, the number of misplaced tiles either remains
constant or decreases by 1. In either case, the consistency requirement is satisfied. Therefore, h1 is consistent. If we
swap the empty tile with an adjacent non-empty tile, then the manhattan distance between the non-empty tile and its
correct position either increases by 1 or decreases by 1. In either case, the consistency requirement is satisfied.
Therefore, h2 is also consistent.

If we have two admissible heuristics hx and hy and hx(n) >= hy(n) for all possible n, then hx dominates hy, and hx is
better for search. In this case, h2 dominates h1 because the manhattan distance between a tile and its correct position
is at least 1.
