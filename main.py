# Jerry Xu
# CS 6364 Spring 2023 Homework 1 (Sliding Puzzle Solver)
# Instructor: Professor Dan Moldovan

import sys
from searchAlgorithms import *
import collections
from utils import *


def main():
    # command line args
    algorithm_name = sys.argv[1]
    input_file_name = sys.argv[2]

    # read the input file
    with open(input_file_name) as f:
        start_state = ''.join(f.readline().split())

    # run the algorithms
    if algorithm_name == 'dfs':
        goal_node, enqueued_states = dfs(start_state)
    elif algorithm_name == 'bfs':
        goal_node, enqueued_states = bfs(start_state)

    # get and print the path from the start state to the goal state
    path_to_goal = collections.deque()
    while goal_node.parent is not None:
        path_to_goal.appendleft(goal_node.state)
        goal_node = goal_node.parent
    path_to_goal.appendleft(start_state)
    pretty_print(enqueued_states, path_to_goal)


if __name__ == "__main__":
    main()
