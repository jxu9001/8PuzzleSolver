from utils import *
from node import *
import heapq

GOAL_STATE = '7816*2543'
MAX_DEPTH = 10


def dfs(root):
    """
    Tree (graph?) search version of DFS with a depth limit of 10.
    OR CAN WE USE GRAPH CAUSE TREE IS TOO ANNOYING (E.G. CYCLES)
    """
    stack = [root]
    expanded_states = {root.state}
    enqueued_states = 0

    while stack:
        curr_node = stack.pop()
        if curr_node.state == GOAL_STATE:
            return curr_node, enqueued_states
        if curr_node.depth > MAX_DEPTH:
            return -1, enqueued_states
        for next_state, step_cost in get_successors(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                next_node = Node(next_state, curr_node, curr_node.path_cost + step_cost, curr_node.depth + 1)
                stack.append(next_node)
                enqueued_states += 1

    return -2, enqueued_states


def bfs(root):
    """
    Simple implementation of breadth-first search.
    """
    queue = collections.deque([root])
    expanded_states = {root.state}
    enqueued_states = 0

    while queue:
        curr_node = queue.popleft()
        if curr_node.state == GOAL_STATE:
            return curr_node, enqueued_states
        if curr_node.depth > MAX_DEPTH:
            return -1, enqueued_states
        for next_state, step_cost in get_successors(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                next_node = Node(next_state, curr_node, curr_node.path_cost + step_cost, curr_node.depth + 1)
                queue.append(next_node)
                enqueued_states += 1

    return -2, enqueued_states


def ids(start_state):
    pass


def astar1(root):
    priority_queue = [(float('inf'), root)]
    heapq.heapify(priority_queue)
    expanded_states = {root.state}
    enqueued_states = 0

    while priority_queue:
        _, curr_node = heapq.heappop(priority_queue)
        if curr_node.state == GOAL_STATE:
            return curr_node, enqueued_states
        if curr_node.depth > MAX_DEPTH:
            return -1, enqueued_states
        for next_state, step_cost in get_successors(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                cost = curr_node.path_cost + step_cost
                next_node = Node(next_state, curr_node, cost, curr_node.depth + 1)
                heapq.heappush(priority_queue, (cost + heuristic1(next_state), next_node))
                enqueued_states += 1

    return -2, enqueued_states


def astar2(root):
    priority_queue = [(float('inf'), root)]
    heapq.heapify(priority_queue)
    expanded_states = {root.state}
    enqueued_states = 0

    while priority_queue:
        _, curr_node = heapq.heappop(priority_queue)
        if curr_node.state == GOAL_STATE:
            return curr_node, enqueued_states
        if curr_node.depth > MAX_DEPTH:
            return -1, enqueued_states
        for next_state, step_cost in get_successors(curr_node.state):
            if next_state not in expanded_states:
                expanded_states.add(next_state)
                cost = curr_node.path_cost + step_cost
                next_node = Node(next_state, curr_node, cost, curr_node.depth + 1)
                heapq.heappush(priority_queue, (cost + heuristic2(next_state), next_node))
                enqueued_states += 1

    return -2, enqueued_states
