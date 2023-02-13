from node import Node
from utils import *
import heapq


def dfs(root, max_depth=MAX_DEPTH):
    """
    Depth-first search with a depth limit of 10
    """
    stack = [root]
    expanded_states = {root.state}
    num_enqueued_states = 0

    while stack:
        curr_node = stack.pop()
        if curr_node.state == GOAL_STATE:
            return curr_node, num_enqueued_states
        if curr_node.depth > max_depth:
            return -1, num_enqueued_states
        for next_state in get_successors(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                next_node = Node(next_state, curr_node, curr_node.depth + 1)
                stack.append(next_node)
                num_enqueued_states += 1

    return -1, num_enqueued_states


def bfs(root):
    """
    Breadth-first search with no depth limit
    (not actually required, but useful for sanity checking)
    """
    queue = collections.deque([root])
    expanded_states = {root.state}
    num_enqueued_states = 0

    while queue:
        curr_node = queue.popleft()
        if curr_node.state == GOAL_STATE:
            return curr_node, num_enqueued_states
        for next_state in get_successors(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                next_node = Node(next_state, curr_node, curr_node.depth + 1)
                queue.append(next_node)
                num_enqueued_states += 1

    return -1, num_enqueued_states


def ids(root, max_depth=MAX_DEPTH):
    """
    Iterative deepening search with a depth limit of 10
    """
    num_enqueued_states = 0

    for depth in range(max_depth + 1):
        # start building the search tree up to depth
        stack = [root]
        expanded_states = {root.state}
        while stack:
            curr_node = stack.pop()
            if curr_node.state == GOAL_STATE:
                return curr_node, num_enqueued_states
            # ONLY ENQUEUE SUCCESSOR STATES IF CURR STATE'S DEPTH IS BELOW THE CURR DEPTH LIMIT
            if curr_node.depth < depth:
                for next_state in get_successors(curr_node.state):
                    if next_state not in expanded_states:
                        expanded_states.add(next_state)
                        next_node = Node(next_state, curr_node, curr_node.depth + 1)
                        stack.append(next_node)
                        num_enqueued_states += 1

    return -1, num_enqueued_states


def astar1(root, max_depth=MAX_DEPTH):
    """
    A* search with heuristic 1 (number of misplaced tiles) and a depth limit of 10
    """
    priority_queue = [(heuristic1(root.state), root)]
    heapq.heapify(priority_queue)
    expanded_states = {root.state}
    num_enqueued_states = 0

    while priority_queue:
        _, curr_node = heapq.heappop(priority_queue)
        if curr_node.state == GOAL_STATE:
            return curr_node, num_enqueued_states
        if curr_node.depth > max_depth:
            return -1, num_enqueued_states
        for next_state in get_successors(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                # g(n) = curr_node.depth + 1
                # h(n) = heuristic(next_state)
                # f(n) = g(n) + h(n)
                next_node = Node(next_state, curr_node, curr_node.depth + 1)
                heapq.heappush(priority_queue, (curr_node.depth + 1 + heuristic1(next_state), next_node))
                num_enqueued_states += 1

    return -1, num_enqueued_states


def astar2(root, max_depth=MAX_DEPTH):
    """
    A* search with heuristic 2 (sum of manhattan distances from tile's current position to its correct position)
    and a depth limit of 10
    """
    priority_queue = [(heuristic2(root.state), root)]
    heapq.heapify(priority_queue)
    expanded_states = {root.state}
    num_enqueued_states = 0

    while priority_queue:
        _, curr_node = heapq.heappop(priority_queue)
        if curr_node.state == GOAL_STATE:
            return curr_node, num_enqueued_states
        if curr_node.depth > max_depth:
            return -1, num_enqueued_states
        for next_state in get_successors(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                # g(n) = curr_node.depth + 1
                # h(n) = heuristic(next_state)
                # f(n) = g(n) + h(n)
                next_node = Node(next_state, curr_node, curr_node.depth + 1)
                heapq.heappush(priority_queue, (curr_node.depth + 1 + heuristic2(next_state), next_node))
                num_enqueued_states += 1

    return -1, num_enqueued_states
