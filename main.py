# Jerry Xu
# CS 6364 Spring 2023 Homework 1 (Sliding Puzzle Solver)
# Instructor: Professor Dan Moldovan

import sys
from searchAlgorithms import *
import collections
from utils import *
from node import *


def main():
    # command line args
    algorithm_name = sys.argv[1]
    input_file_name = sys.argv[2]

    # read the input file
    with open(input_file_name) as f:
        start_state = ''.join(f.readline().split())
    root = Node(state=start_state)

    # run the algorithms
    assert algorithm_name in ('dfs', 'bfs', 'ids', 'astar1', 'astar2')
    if algorithm_name == 'dfs':
        goal_node, enqueued_states = dfs(root)
    elif algorithm_name == 'bfs':
        goal_node, enqueued_states = bfs(root)
    # elif algorithm_name == 'ids':
    #     pass
    elif algorithm_name == 'astar1':
        goal_node, enqueued_states = astar1(root)
    else:
        goal_node, enqueued_states = astar2(root)

    # get and print the path from the start state to the goal state
    pretty_print(goal_node, enqueued_states)


if __name__ == "__main__":
    main()
