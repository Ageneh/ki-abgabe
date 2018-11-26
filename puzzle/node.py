class Node:
	"""
	A simple node class. Can be used to create a tree-like structure.
	"""
	_l, _r, _u, _d = "left", "right", "up", "down"
	__keys = [_l, _u, _d, _r]
	empty = 0

	def __init__(self, data):
		self._data = None
		# self._children = { k:None for k in Node.__keys }
		self._children = {}
		self.set_data(data)
		self.set_depth(0)

	def set_data(self, data):
		self._data = data

	def depth(self): return self._depth

	def expand(self):
		data = self.children()
		children = list(filter(lambda x: x is not None and x._data, list(self.children().values())))
		for c in children:
			c.set_parent(parent=self)
			c.set_depth(self._depth + 1)

		return children

	def set_depth(self, depth):
		self._depth = depth

	def set_children(self):
		self._empty_x, self._empty_y = self.get_empty()
		empty_x, empty_y = self._empty_x, self._empty_y

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

		self._children[self._l] = Node(left)
		self._children[self._u] = Node(up)
		self._children[self._d] = Node(down)
		self._children[self._r] = Node(right)

		return self._children

	def get_empty(self):
		for row in self._data:
			if self.empty in row:
				x, y = row.index(self.empty), self._data.index(row)
				return x, y

	def data_copy(self):
		copy = []
		for lst in self._data:
			copy.append([ele for ele in lst])
		return copy

	def children(self):
		return self.set_children()

	def key(self):
		return self._data

	def parent(self):
		return self._parent if hasattr(self, "_parent") else None

	def set_parent(self, parent=None):
		self._parent = parent

	def set_move(self, direction):
		self._move = str(direction) if type(direction) is str else direction

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return "Node({})".format(self._data)

	def __eq__(self, other):
		return self.__hash__() == other.__hash__()

	def __hash__(self):
		return hash((str(self._data)))

	def __gt__(self, other):
		return self.__hash__() > other.__hash__()

	def __lt__(self, other):
		return self.__hash__() < other.__hash__()
