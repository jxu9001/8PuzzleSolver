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
        for next_state in get_next_state(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                next_node = Node(state=next_state, parent=curr_node, depth=curr_node.depth + 1)
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
        for next_state in get_next_state(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                next_node = Node(state=next_state, parent=curr_node, depth=curr_node.depth + 1)
                queue.append(next_node)
                num_enqueued_states += 1

    return -1, num_enqueued_states


def ids(root, max_depth=MAX_DEPTH):
    """
    Iterative deepening search with a depth limit of 10
    """
    num_enqueued_states = 0

    for depth in range(max_depth + 1):
        stack = [root]
        expanded_states = {root.state}
        while stack:
            curr_node = stack.pop()
            if curr_node.state == GOAL_STATE:
                return curr_node, num_enqueued_states
            # only enqueue successor states if we have not reached the depth limit
            if curr_node.depth < depth:
                for next_state in get_next_state(curr_node.state):
                    if next_state not in expanded_states:
                        expanded_states.add(next_state)
                        next_node = Node(state=next_state, parent=curr_node, depth=curr_node.depth + 1)
                        stack.append(next_node)
                        num_enqueued_states += 1

    return -1, num_enqueued_states


def astar(root, heuristic, max_depth=MAX_DEPTH):
    """
    A* search with two different heuristics and a depth limit of 10
    """
    priority_queue = [(heuristic1(root.state), root)] if heuristic == 1 else [(heuristic2(root.state), root)]
    heapq.heapify(priority_queue)
    expanded_states = {root.state}
    num_enqueued_states = 0

    while priority_queue:
        _, curr_node = heapq.heappop(priority_queue)
        if curr_node.state == GOAL_STATE:
            return curr_node, num_enqueued_states
        if curr_node.depth > max_depth:
            return -1, num_enqueued_states
        for next_state in get_next_state(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                # g(n) = curr_node.depth + 1
                # h(n) = heuristic(next_state)
                # f(n) = g(n) + h(n)
                next_node = Node(state=next_state, parent=curr_node, depth=curr_node.depth + 1)
                if heuristic == 1:
                    total_cost = curr_node.depth + 1 + heuristic1(next_state)
                elif heuristic == 2:
                    total_cost = curr_node.depth + 1 + heuristic2(next_state)
                heapq.heappush(priority_queue, (total_cost, next_node))
                num_enqueued_states += 1

    return -1, num_enqueued_states
