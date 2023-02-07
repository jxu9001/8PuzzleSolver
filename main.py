# Jerry Xu
# CS 6364 Spring 2023 Homework 1 (Sliding Puzzle Solver)
# Instructor: Professor Dan Moldovan

import sys
from searchAlgorithms import *
from utils import *


def main():
    # command line args
    algorithm_name = sys.argv[1]
    input_file_name = sys.argv[2]

    # read the input file
    with open(input_file_name) as f:
        start_state = ''.join(f.readline().split())

    if algorithm_name == 'dfs':
        moves, enqueued_states, path_to_goal = dfs(start_state)
    elif algorithm_name == 'bfs':
        moves, enqueued_states, path_to_goal = bfs(start_state)
    pretty_print(moves, enqueued_states, path_to_goal)


if __name__ == "__main__":
    main()
