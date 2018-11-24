class Node:
	"""
	A simple node class. Can be used to create a tree-like structure.
	"""

	def __init__(self, data, children=[]):
		self.data = data
		self.children = set()
		self.add_child(nodes=children)

	def add_child(self, node=None, nodes=None):
		"""
		Add a new child node to this node.
		Either just one child or a list of child nodes can be added.
		Node must be of type Node and also must not be None.
		"""
		lst = []
		if node and type(node) is Node: lst.append(node)
		if nodes and len(nodes) > 0:
			for n in nodes:
				if n and type(n) is Node: lst.append(n)

		for n in lst:
			if type(n) is Node: self.children.add(n)

	def insert_child(self, index, node):
		"""
		Add a new child node to this node.
		Either just one child or a list of child nodes can be added.
		Node must be of type Node and also must not be None.
		"""
		self.children

	def rm_child(self, node):
		"""Remove a child node from this node."""
		self.children.remove(node)

	def next_child(self):
		"""Get the next child """
		for n in self.children: yield n

	def __repr__(self):
		if len(self.children) == 0: return "Node({})".format(self.data)
		return "Node({}, children={})".format(self.data, self.children)

	def __str__(self):
		if len(self.children) == 0:
			return "Node({})".format(self.data, self.children)
		return "Node({}, {})".format(self.data, self.children).replace("set", "")
