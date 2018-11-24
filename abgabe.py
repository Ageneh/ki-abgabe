from queue import Queue

from node import Node

def breadthfirst(queue, nodes):



	return

if __name__ == '__main__':
	root = Node(1)
	two = Node(2)
	three = Node(3)
	four = Node(4)
	five = Node(5)
	six = Node(6)
	seven = Node(7)
	goal = Node(0)

	root.add_child(two)
	root.add_child(three)
	root.add_child(four)

	two.add_child(five)

	three.add_child(six)

	four.add_child(six)

	five.add_child(root)

	six.add_child(seven)
	six.add_child(goal)

	print(str(root))

	queue = Queue(5)

	breadthfirst(queue, root)


