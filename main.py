# Jerry Xu
# CS 6364 Spring 2023 Homework 1 (Sliding Puzzle Solver)

import collections
import sys

GOAL_STATE = '7816*2543'


def get_successors(state):
    """
    Function that returns the successor states of a given state. A successor state is found by sliding a single tile.

    :param state: a configuration of an 8-piece sliding puzzle represented as a string. We represent
    for example, the following state
        +---+---+---+
        | 6 | 7 | 1 |
        +---+---+---+
        | 8 | 2 |   |
        +---+---+---+
        | 5 | 4 | 3 |
        +---+---+---+
    is represented as the string '67182*543'
    :return: all possible successor states of the given state represented as strings
    """
    swap_locations = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7],
    }

    empty_space = state.find('*')
    for location in swap_locations[empty_space]:
        s = list(state)
        s[location], s[empty_space] = s[empty_space], s[location]
        yield ''.join(s)


def bfs(start_state):
    """
    Simple implementation of breadth-first search.

    :param start_state: starting configuration of the puzzle
    :return: the number of moves required to solve the puzzle and the number of states enqueued.
    If the starting configuration has no solution, return -1.
    """
    queue = collections.deque([(start_state, 0)])
    visited = {start_state}
    enqueued_states = 0

    while queue:
        state, moves = queue.popleft()
        if state == GOAL_STATE:
            return moves, enqueued_states
        for next_state in get_successors(state):
            if next_state in visited:
                continue
            visited.add(next_state)
            queue.append((next_state, moves + 1))
            enqueued_states += 1

    return -1, enqueued_states


def main():
    # command line args
    algorithm_name = sys.argv[1]
    input_file_name = sys.argv[2]

    # read the input file
    with open(input_file_name) as f:
        start_state = ''.join(f.readline().split())

    print(bfs(start_state))


if __name__ == "__main__":
    main()