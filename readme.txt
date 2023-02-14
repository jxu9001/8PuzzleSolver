Jerry Xu
CS 6364 Spring 2023
Homework 1 README

*** INSTRUCTIONS TO RUN THE SOLVER ***
To run the solver, first ensure that the *.py files and the input files are in the same directory.
Next, type "python3 main.py <algorithm_name> <input_file_name>" into the terminal and press enter.
algorithm_name is one of:
    dfs (depth first search)
    bfs (breadth first search (not required, but useful to calculate the # of moves in the optimal solutions))
    ids (iterative deepening search)
    astar1 (a* search with heuristic 1)
    astar2 (a* search with heuristic 2)
input_file_name is one of:
    input1.txt (easy, optimal solution has 5 moves)
    input2.txt (medium, optimal solution has 9 moves)
    input3.txt (hard, optimal solution has 12 moves)
    input4.txt (very hard, optimal solution has 30 moves)

*** SAMPLE INPUT AND OUTPUTS FOR INPUT2.TXT ***
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
    h1: total # of misplaced tiles
    h2: Σ(manhattan distance from each tile to its goal position)

Both h1 and h2 clearly underestimate of the moves needed to move a misplaced tile to its correct position. h1 assumes
that it takes one move to do so, and h2 does not account for the non-empty tiles between the misplaced tile and its
correct position. Thus, both h1 and h2 are admissible.

By definition, a heuristic h(n) is consistent if h(n) <= path_cost(n, n') + h(n'). In this problem, the path_cost is 1
because state n' is generated from state n by swapping the empty tile with an adjacent tile. Thus, consistency requires
that h(n) - h(n') <= 1. If we swap the empty tile with an adjacent tile, the number of misplaced tiles either remains
constant or decreases by 1. In either case, the consistency requirement is satisfied. Therefore, h1 is consistent. If we
swap the empty tile with an adjacent non-empty tile, then the manhattan distance between the non-empty tile and its
correct position either increases by 1 or decreases by 1. In either case, the consistency requirement is satisfied.
Therefore, h2 is also consistent.

If we have two admissible heuristics hx and hy and hx(n) >= hy(n) for all possible n, then hx dominates hy, and hx is
better for search. In this case, h2 dominates h1 because the manhattan distance between a tile and its correct position
is at least 1.
