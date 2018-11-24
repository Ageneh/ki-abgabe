from queue import Queue
from node import Node

def breadthfirst(queue, node):

	children = node.children()
	for c in children:
		breadthfirst(queue, c)
		print(node._data)

	return

def search(start, goal):
	from time import sleep

	queue = [start]
	reached = [start]

	while queue:
		state = queue.pop(0)
		if state is goal:
			return state

		reached.append(state)
		ex = state.expand()
		newex = [s for s in ex if s not in reached]
		print("state:", state, "\t>\tnewex:", newex, "\t>\tchildren:", state.children())
		for e in newex:
			queue.append(e)
		a = 0
		sleep(1)


	return None

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
	print(search(root, goal))


