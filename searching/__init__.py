from searching import search
from searching.node import Node
from searching.search import breadthfirst, depthfirst, search, path


if __name__ == '__main__':
	_root = Node(1, root=True)
	two = Node(2)
	three = Node(3)
	four = Node(4)
	five = Node(5)
	six = Node(6)
	seven = Node(7)
	_goal = Node(0)

	_root.add_child(two)
	_root.add_child(three)
	_root.add_child(four)
	two.add_child(five)
	three.add_child(six)
	four.add_child(six)
	five.add_child(_root)
	six.add_child(seven)
	six.add_child(_goal)

	print("breadthfirst asc")
	result = search(_root, _goal, strategy=breadthfirst, desc=False, v=True)

	solution = path(result)
	print({(solution.index(n)+1, n) for n in solution})

	# print("--"*60)
	# print("breadthfirst desc")
	# search(_root, _goal, strategy=breadthfirst, desc=True, v=True)
	# print("")
	# print("//"*60)
	# print("")
	# print("depthfirst asc")
	# search(_root, _goal, strategy=depthfirst, desc=False, v=True)
	# print("--"*60)
	# print("depthfirst desc")
	# search(_root, _goal, strategy=depthfirst, desc=True, v=True)