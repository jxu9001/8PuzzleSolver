# Jerry Xu
# CS 6364 Spring 2023 Homework 1 (8 Puzzle Solver)
# Instructor: Professor Dan Moldovan

from search_algorithms import *
from utils import *
from sys import argv


def main():
    # command line args
    algorithm_name = argv[1]
    input_file_name = argv[2]

    # read the input file
    with open(input_file_name) as f:
        start_state = ''.join(f.readline().split())
    root = Node(state=start_state)

    # run the algorithms
    assert algorithm_name in ('dfs', 'bfs', 'ids', 'astar1', 'astar2')
    if algorithm_name == 'dfs':
        goal_node, num_enqueued_states = dfs(root)
    elif algorithm_name == 'bfs':
        goal_node, num_enqueued_states = bfs(root)
    elif algorithm_name == 'ids':
        goal_node, num_enqueued_states = ids(root)
    elif algorithm_name == 'astar1':
        goal_node, num_enqueued_states = astar(root, 1)
    else:
        goal_node, num_enqueued_states = astar(root, 2)

    # get and print the path from the start state to the goal state
    pretty_print(goal_node, num_enqueued_states)


if __name__ == "__main__":
    main()
