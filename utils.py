import collections
MAX_DEPTH = 10
GOAL_STATE = '7816*2543'


def pretty_print(goal_node, num_enqueued_states):
    """
    Pretty prints the path from the start state to the goal state.
    """
    if goal_node == -1:
        print('ERROR: Failed to find a solution at or before depth = {}'.format(MAX_DEPTH))
    else:
        path_to_goal = collections.deque()
        while goal_node is not None:
            path_to_goal.appendleft(goal_node.state)
            goal_node = goal_node.parent
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
            print()

        print('Number of moves = {}'.format(n - 1))
        print('Number of states enqueued = {}\n'.format(num_enqueued_states))
        print('Note: * represents an empty tile')


def get_successors(state):
    """
    For a given state, return the next states and step costs.
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
        next_state = ''.join(s)
        yield next_state


def heuristic1(state, goal_state=GOAL_STATE):
    """
    Heuristic 1: number of misplaced tiles
    Note that the blank tile is not actually a tile so we don't count it
    """
    return sum(t1 != t2 for t1, t2 in zip(state, goal_state) if t1.isdigit())


def heuristic2(state, goal_state=GOAL_STATE):
    """
    Heuristic 2: sum of manhattan distances from each tile's curr position to its goal position
    Note that the blank tile is not actually a tile so we don't count it
    """
    # formula to convert 1d array index to 2d array index when 2d array has dims num_rows, num_cols
    # i = 1d // num_cols, j = 1d % num_rows
    goal_pos = {
        '1': (goal_state.find('1') // 3, goal_state.find('1') % 3),
        '2': (goal_state.find('2') // 3, goal_state.find('2') % 3),
        '3': (goal_state.find('3') // 3, goal_state.find('3') % 3),
        '4': (goal_state.find('4') // 3, goal_state.find('4') % 3),
        '5': (goal_state.find('5') // 3, goal_state.find('5') % 3),
        '6': (goal_state.find('6') // 3, goal_state.find('6') % 3),
        '7': (goal_state.find('7') // 3, goal_state.find('7') % 3),
        '8': (goal_state.find('8') // 3, goal_state.find('8') % 3)
    }

    return sum(abs(i // 3 - goal_pos[t][0]) + abs(i % 3 - goal_pos[t][1]) for i, t in enumerate(state) if t.isdigit())
