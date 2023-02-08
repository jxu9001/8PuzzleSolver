class Node:
    def __init__(self, state=None, parent=None, path_cost=1, depth=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.depth = depth
