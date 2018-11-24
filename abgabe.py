from queue import Queue
from node import Node


def breadthfirst(start, goal, v=False):
	queue = [start]
	reached = [start]

	while queue:
		state = queue.pop(0)
		if state is goal:
			if v: print("state:", state, "\t>\tnewex:", newex, "\t>\tchildren:", state.children())
			return state

		reached.append(state)
		ex = state.expand()
		newex = [s for s in ex if s not in reached]
		for e in newex:
			queue.append(e)

		if v:
			print("state:", state, "\t>\tnewex:", newex, "\t>\tchildren:", state.children())
			sleep()

	return None


def depthfirst(start, goal, v=False):
	stack = [start]
	reached = [start]

	while stack:
		state = stack.pop(0)
		if state is goal:
			if v: print("state:", state, "\t>\tnewex:", newex, "\t>\tchildren:", state.children())
			return state

		reached.append(state)
		ex = state.expand()
		newex = [s for s in ex if s not in reached]
		for e in newex:
			stack.insert(0, e)

		if v:
			print("state:", state, "\t>\tnewex:", newex, "\t>\tchildren:", state.children())
			sleep()

	return None


def sleep():
	from time import sleep
	sleep(0.2)

def search(start, goal, strategy, asc=True, v=False):
	queue = [start]
	reached = [start]

	while queue:
		state = queue.pop(0)
		if state is goal:
			if v: print("state:", state, "\t>\tnewex:", state.children())
			return state

		reached.append(state)
		ex = state.expand()
		newex = [s for s in ex if s not in reached]
		queue = strategy(queue, newex)

		if v:
			print("state:", state, "\t>\tnewex:", newex, "\t>\tchildren:", state.children())
			sleep()

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
	print(breadthfirst(root, goal, v=True))
	print("")
	print(depthfirst(root, goal, v=True))
