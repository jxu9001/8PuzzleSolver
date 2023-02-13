# def pretty_print(moves, enqueued_states, path_to_goal):
#     """
#     Pretty prints the path from the start state to the goal state.
#     """
#     n = len(path_to_goal)
#     print('Input (Any random position of the tiles):\n')
#     for j in [0, 3, 6]:
#         print(' '.join(list(path_to_goal[0][j:j + 3])))
#     print('\nOutput (List of states starting from input to goal state, if found):\n')
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


def pretty_print(enqueued_states, path_to_goal):
    """
    Pretty prints the path from the start state to the goal state.
    """
    n = len(path_to_goal)
    print('Input (Any random position of the tiles):\n')
    for j in [0, 3, 6]:
        print(' '.join(list(path_to_goal[0][j:j + 3])))
    print('\nOutput (List of states starting from input to goal state, if found):\n')
    for i, state in enumerate(path_to_goal):
        for j in [0, 3, 6]:
            row = ' '.join(list(state[j:j + 3]))
            if i == 0 and j == 0:
                row += ' (Initial input state)'
            if i == n - 1 and j == 0:
                row += ' (Goal state)'
            print(row)
        print('')
    print('Number of moves = {}'.format(len(path_to_goal) - 1))
    print('Number of states enqueued = {}\n'.format(enqueued_states))
    print('Note: * represents an empty tile')


def get_successors(state):
    """
    Function that returns the successor states of a given state.
    A successor state is found by swapping the empty tile with one of its neighbors.
    States are represented as strings b/c strings are hashable (i.e., they can be added to python sets).
    For example, the following state
        +---+---+---+
        | 6 | 7 | 1 |
        +---+---+---+
        | 8 | 2 |   |
        +---+---+---+
        | 5 | 4 | 3 |
        +---+---+---+
    is represented by the string '67182*543'.
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
        8: [5, 7]
    }

    empty_space = state.find('*')
    for location in swap_locations[empty_space]:
        s = list(state)
        s[location], s[empty_space] = s[empty_space], s[location]
        yield ''.join(s)
