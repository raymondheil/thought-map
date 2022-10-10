# node.py
# DESCRIPTION WOULD GO HERE I HOPE

import itertools

class Node:
    'Base class for all nodes on the map'
    id_iter = itertools.count() # Let all nodes have a unique id
    def __init__(self):
        self.name = name
        self.desc = desc
        self.parents = [] # Would ETE be helpful with this? Maybe, maybe not 
        self.children = []
        self.id = next(Node.id_iter)

class Thought(Node):
    'A single thought on the map, with a text description'
    def __init__(self, desc):
        super().__init__(self)
        self.desc = desc

