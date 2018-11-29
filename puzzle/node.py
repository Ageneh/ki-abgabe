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

	def depth(self): return self._depth

	def expand(self):
		data = self.children()
		children = list(filter(lambda x: x and x._data, list(self.children().values())))

		return children

	def children(self):
		if len(self._children.values()) > 1:
			return self._children
		return self.set_children()

	def parent(self):
		return self._parent if hasattr(self, "_parent") else None

	def data_copy(self):
		copy = []
		for lst in self._data:
			copy.append([ele for ele in lst])
		return copy

	def is_root(self): return self._root

	def is_goal(self): return self._goal

	def get_empty(self):
		"""Returns a tuple containing the x and y coordinates of the empty space."""
		for row in self._data:
			if self._empty in row:
				x, y = row.index(self._empty), self._data.index(row)
				return x, y

	def set_data(self, data):
		self._data = data

	def set_depth(self, depth): self._depth = depth

	def set_children(self):
		empty_x, empty_y = self.get_empty()

		if empty_x > 0:
			left = self.data_copy()
			left[empty_y][empty_x], left[empty_y][empty_x - 1] = left[empty_y][empty_x - 1], left[empty_y][empty_x]
		else: left = None

		if empty_x < len(self._data) - 1:
			right = self.data_copy()
			right[empty_y][empty_x], right[empty_y][empty_x + 1] = right[empty_y][empty_x + 1], right[empty_y][empty_x]
		else: right = None

		## up/down
		if empty_y > 0:
			up = self.data_copy()
			up[empty_y][empty_x], up[empty_y - 1][empty_x] = up[empty_y - 1][empty_x], up[empty_y][empty_x]
		else: up = None

		if empty_y < len(self._data) - 1:
			down = self.data_copy()
			down[empty_y][empty_x], down[empty_y + 1][empty_x] = down[empty_y + 1][empty_x], down[empty_y][empty_x]
		else: down = None

		n_depth = self._depth + 1
		self._children[self._l] = Node(left, direction=self._l, depth=n_depth, parent=self)
		self._children[self._u] = Node(up, direction=self._u, depth=n_depth, parent=self)
		self._children[self._d] = Node(down, direction=self._d, depth=n_depth, parent=self)
		self._children[self._r] = Node(right, direction=self._r, depth=n_depth, parent=self)

		return self._children

	def set_parent(self, parent=None): self._parent = parent

	def set_move(self, direction):
		self._move = str(direction) if type(direction) is str else direction

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return "Node({}, root={}, goal={})".format(self._data, self._root, self._goal)

	def __eq__(self, other):
		return self.__hash__() == other.__hash__()

	def __hash__(self):
		return hash((str(self._data)))
