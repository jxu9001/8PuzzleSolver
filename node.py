class Node:
    """
    Class to represent nodes in the search tree based on section 3.3 of Russell and Norvig (3rd Edition)
    We don't need an action parameter b/c it's trivial to infer the action given a state and its successor
    We don't need a path_cost parameter b/c path_cost = depth for this particular problem
    """
    def __init__(self, state=None, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

    def __lt__(self, other):
        return self.depth < other.depth
