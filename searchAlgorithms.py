import collections
from utils import *

# for some reason, the professor defined the goal state as this:
# +---+---+---+
# | 7 | 8 | 1 |
# +---+---+---+
# | 6 |   | 2 |
# +---+---+---+
# | 5 | 4 | 3 |
# +---+---+---+
# instead of this:
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 7 | 8 |   |
# +---+---+---+
GOAL_STATE = '7816*2543'
MAX_DEPTH = 10


def dfs(start_state):
    """
    DFS with a depth limit of 10.
    """
    stack = [(start_state, 0, [])]
    visited = {start_state}
    enqueued_states = 0

    while stack:
        curr_state, moves, path_to_goal = stack.pop()
        if curr_state == GOAL_STATE:
            return moves, enqueued_states, path_to_goal + [curr_state]
        # if moves > MAX_DEPTH:
        #     return -1, enqueued_states, path_to_goal
        for next_state in get_successors(curr_state):
            if next_state in visited:
                continue
            visited.add(next_state)
            stack.append((next_state, moves + 1, path_to_goal + [curr_state]))
            enqueued_states += 1

    return -1, enqueued_states, path_to_goal


def bfs(start_state):
    """
    Simple implementation of breadth-first search.
    """
    queue = collections.deque([(start_state, 0, [])])
    visited = {start_state}
    enqueued_states = 0

    while queue:
        curr_state, moves, path_to_goal = queue.popleft()
        if curr_state == GOAL_STATE:
            return moves, enqueued_states, path_to_goal + [curr_state]
        for next_state in get_successors(curr_state):
            if next_state in visited:
                continue
            visited.add(next_state)
            queue.append((next_state, moves + 1, path_to_goal + [curr_state]))
            enqueued_states += 1

    return -1, enqueued_states, path_to_goal
