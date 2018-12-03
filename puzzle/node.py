class Node:
    """
    A simple node class. Can be used to create a tree-like structure.
    """
    _l, _r, _u, _d = "left", "right", "up", "down"
    __keys = [_l, _u, _d, _r]
    _empty = 0

    def __init__(self, data, root=False, goal=False, depth=0, direction=None, parent=None):
        self._children = {}
        self.set_data(data)
        self.set_depth(depth)
        self.set_move(direction)
        self.set_parent(parent)
        self._root = True if root else False
        self._goal = True if goal else False

    def depth(self):
        return self._depth

    def expand(self):
        """Expands a node and returns its adjacent nodes."""
        self._children = self.children()
        return list(filter(lambda x: x and x._data, list(self.children().values())))

    def children(self):
        if len(self._children.values()) > 1:
            return self._children
        return self.set_children()

    def parent(self):
        return self._parent if hasattr(self, "_parent") else None

    def data_copy(self):
        """Copies data from a node in a new list and returns the copy."""
        copy = []
        for lst in self._data:
            copy.append([ele for ele in lst])
        return copy

    def path(self, reversed=False):
        """Returns a list containing all steps. Either in correct or reversed order."""
        path = [self]
        while path[-1].parent() and not path[-1].is_root():
            path.append(path[-1].parent())
        return path[::-1] if not reversed else path

    def is_root(self):
        return self._root

    def is_goal(self):
        return self._goal

    def get_pos(self, val=_empty):
        """Returns a tuple containing the x and y coordinates of the given value 'val'."""
        for row in self._data:
            if val in row:
                x, y = row.index(val), self._data.index(row)
                return x, y

    def set_data(self, data):
        self._data = data

    def set_depth(self, depth):
        self._depth = depth

    def set_children(self):
        empty_x, empty_y = self.get_pos()

        if empty_x > 0:
            left = self.data_copy()
            left[empty_y][empty_x], left[empty_y][empty_x - 1] = left[empty_y][empty_x - 1], left[empty_y][empty_x]
        else:
            left = None

        if empty_x < len(self._data) - 1:
            right = self.data_copy()
            right[empty_y][empty_x], right[empty_y][empty_x + 1] = right[empty_y][empty_x + 1], right[empty_y][empty_x]
        else:
            right = None

        ## up/down
        if empty_y > 0:
            up = self.data_copy()
            up[empty_y][empty_x], up[empty_y - 1][empty_x] = up[empty_y - 1][empty_x], up[empty_y][empty_x]
        else:
            up = None

        if empty_y < len(self._data) - 1:
            down = self.data_copy()
            down[empty_y][empty_x], down[empty_y + 1][empty_x] = down[empty_y + 1][empty_x], down[empty_y][empty_x]
        else:
            down = None

        n_depth = self._depth + 1
        self._children[self._l] = Node(left, direction=self._l, depth=n_depth, parent=self)
        self._children[self._u] = Node(up, direction=self._u, depth=n_depth, parent=self)
        self._children[self._d] = Node(down, direction=self._d, depth=n_depth, parent=self)
        self._children[self._r] = Node(right, direction=self._r, depth=n_depth, parent=self)

        return self._children

    def set_parent(self, parent=None):
        self._parent = parent

    def set_move(self, direction):
        self._move = str(direction) if type(direction) is str else direction

    def __repr__(self):
        return "Node({}, root={}, goal={}, depth={}, direction={}, parent={})" \
            .format(self._data, self._root, self._goal, self._depth, self._move, self._parent)

	def __str__(self):
		return "Node({}, direction={})".format(self._data, self._move)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((str(self._data)))

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data) if self._data else 0
