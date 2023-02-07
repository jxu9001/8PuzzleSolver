# Jerry Xu
# CS 6364 Spring 2023 Homework 1 (Sliding Puzzle Solver)
# Instructor: Professor Dan Moldovan

import sys
from searchAlgorithms import *
from utils import *

# def pretty_print(moves, enqueued_states, path_to_goal):
#     """
#     Pretty prints the path from the start state to the goal state
#     """
#     n = len(path_to_goal)
#     for i, state in enumerate(path_to_goal):
#         for j in [0, 3, 6]:
#             row = ' '.join(list(state[j:j + 3]))
#             if i == 0 and j == 0:
#                 row += ' (Initial input state)'
#             if i == n - 1 and j == 0:
#                 row += ' (Goal state)'
#             print(row)
#         print('')
#     print('Number of moves = {}'.format(moves))
#     print('Number of states enqueued = {}\n'.format(enqueued_states))
#     print('Note: * represents an empty tile')


# def get_successors(state):
#     """
#     Function that returns the successor states of a given state.
#     A successor state is found by sliding a single tile into the empty space.
#     States are represented as strings so they can be put into python sets.
#     For example, the following state
#         +---+---+---+
#         | 6 | 7 | 1 |
#         +---+---+---+
#         | 8 | 2 |   |
#         +---+---+---+
#         | 5 | 4 | 3 |
#         +---+---+---+
#     is represented by the string '67182*543'.
#     """
#     swap_locations = {
#         0: [1, 3],
#         1: [0, 2, 4],
#         2: [1, 5],
#         3: [0, 4, 6],
#         4: [1, 3, 5, 7],
#         5: [2, 4, 8],
#         6: [3, 7],
#         7: [4, 6, 8],
#         8: [5, 7],
#     }
#
#     empty_space = state.find('*')
#     for location in swap_locations[empty_space]:
#         s = list(state)
#         s[location], s[empty_space] = s[empty_space], s[location]
#         yield ''.join(s)
#
#
# def bfs(start_state):
#     """
#     Simple implementation of breadth-first search.
#     """
#     queue = collections.deque([(start_state, 0, [])])
#     visited = {start_state}
#     enqueued_states = 0
#
#     while queue:
#         state, moves, path_to_goal = queue.popleft()
#         if state == GOAL_STATE:
#             return moves, enqueued_states, path_to_goal
#         for next_state in get_successors(state):
#             if next_state in visited:
#                 continue
#             visited.add(next_state)
#             queue.append((next_state, moves + 1, path_to_goal + [state]))
#             enqueued_states += 1
#
#     return -1, enqueued_states, path_to_goal


def main():
    # command line args
    algorithm_name = sys.argv[1]
    input_file_name = sys.argv[2]

    # read the input file
    with open(input_file_name) as f:
        start_state = ''.join(f.readline().split())

    moves, enqueued_states, path_to_goal = bfs(start_state)
    pretty_print(moves, enqueued_states, path_to_goal)


if __name__ == "__main__":
    main()
