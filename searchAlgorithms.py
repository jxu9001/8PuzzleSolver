import collections
from utils import *
from node import *

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
    Tree search version of DFS with a depth limit of 10.
    OR CAN WE USE GRAPH CAUSE TREE IS TOO ANNOYING (E.G. CYCLES)
    """
    stack = [Node(state=start_state, parent=None, depth=0)]
    visited = {start_state}
    enqueued_states = 0

    while stack:
        curr_node = stack.pop()
        if curr_node.state == GOAL_STATE:
            return curr_node, enqueued_states
        for next_state in get_successors(curr_node.state):
            if next_state in visited:
                continue
            visited.add(next_state)
            stack.append(Node(state=next_state, parent=curr_node, depth=curr_node.depth+1))
            enqueued_states += 1

    return -1, enqueued_states


def bfs(start_state):
    """
    Simple implementation of breadth-first search.
    """
    queue = collections.deque([Node(state=start_state, parent=None, depth=0)])
    visited = {start_state}
    enqueued_states = 0

    while queue:
        curr_node = queue.popleft()
        if curr_node.state == GOAL_STATE:
            return curr_node, enqueued_states
        for next_state in get_successors(curr_node.state):
            if next_state in visited:
                continue
            visited.add(next_state)
            queue.append(Node(state=next_state, parent=curr_node, depth=curr_node.depth+1))
            enqueued_states += 1

    return -1, enqueued_states
