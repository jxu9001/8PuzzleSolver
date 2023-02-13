class Node:
    """
    Class to represent nodes in the search tree per section 3.3 of Russell and Norvig (3rd Edition)
    """
    def __init__(self, state=None, parent=None, path_cost=0, depth=0):
        self.state = state
        self.parent = parent
        '''
        NB: this is the cost from the root of the search tree to this node
        not the cost from this node's parent to this node
        '''
        self.path_cost = path_cost
        self.depth = depth

    def __lt__(self, other):
        return self.path_cost < other.path_cost
