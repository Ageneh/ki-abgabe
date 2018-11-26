class Node:
    """
    A simple node class. Can be used to create a tree-like structure.
    """

    def __init__(self, data, children=[]):
        self._data = None
        self._children = set()
        self.set_data(data)
        self.add_child(nodes=children)

    def set_data(self, data):
        self._data = data

    def add_child(self, node=None, nodes=None):
        """
        Add a new child node to this node.
        Either just one child or a list of child nodes can be added.
        Node must be of type Node and also must not be None.
        """
        lst = []
        if node and type(node) is Node:
            lst.append(node)
        if nodes and len(nodes) > 0:
            for n in nodes:
                if n and type(n) is Node:
                    lst.append(n)

        for n in lst:
            if type(n) is Node:
                self._children.add(n)

    def insert_child(self, index, node):
        """
        Add a new child node to this node.
        Either just one child or a list of child nodes can be added.
        Node must be of type Node and also must not be None.
        """
        if index and node and type(node) is Node:
            content = list(self._children)
            self._children.clear()
            content.insert(index, node)
            for n in content: self._children.add(n)

    def rm_child(self, node):
        """Remove a child node from this node."""
        self._children.remove(node)

    def next_child(self):
        """Get the next child """
        for n in self._children: yield n

    def expand(self):
        return list(self.children())

    def children(self):
        return self._children

    def key(self):
        return self._data

    def __repr__(self):
        # if len(self._children) == 0: return "Node({})".format(self._data)
        # return "Node({}, children={})".format(self._data, self._children)
        return self.__str__()

    def __str__(self):
        return "Node({})".format(self._data)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self._data, str(self._children)))

    def __gt__(self, other):
        return self.__hash__() > other.__hash__()

    def __lt__(self, other):
        return self.__hash__() < other.__hash__()
