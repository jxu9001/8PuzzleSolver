import collections
from utils import *

GOAL_STATE = '7816*2543'


def bfs(start_state):
    """
    Simple implementation of breadth-first search.
    """
    queue = collections.deque([(start_state, 0, [])])
    visited = {start_state}
    enqueued_states = 0

    while queue:
        state, moves, path_to_goal = queue.popleft()
        if state == GOAL_STATE:
            return moves, enqueued_states, path_to_goal
        for next_state in get_successors(state):
            if next_state in visited:
                continue
            visited.add(next_state)
            queue.append((next_state, moves + 1, path_to_goal + [state]))
            enqueued_states += 1

    return -1, enqueued_states, path_to_goal