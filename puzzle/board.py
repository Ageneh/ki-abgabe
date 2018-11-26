from puzzle.node import Node

_max_depth = 50


def breadthfirst(queue, expanded):
	for e in expanded:
		queue.append(e)
	return queue


def depthfirst(stack, expanded):
	for e in expanded:
		stack.insert(0, e)
	return stack


def path(node, reversed=False):
	path = [node]
	while path[-1].parent():
		path.append(path[-1].parent())
	return path[::-1] if not reversed else path


def solve(start, goal, strategy=breadthfirst):
	queue = [start]
	reached = [start]

	while queue:
		state = queue.pop(0)

		if state.depth() >= 6: continue

		if state == goal:
			return path(state), len(reached)

		reached.append(state)
		children = state.expand()
		newex = [s for s in children if s not in reached]

		queue = strategy(queue, newex)

	return None


u_cost = 1

if __name__ == '__main__':
	init = [
		[2, 8, 3],
		[1, 6, 4],
		[7, 0, 5],
	]
	final = [
		[1, 2, 3],
		[8, 0, 4],
		[7, 6, 5],
	]

	root = Node(init)
	goal = Node(final)

	result, path_len = solve(root, goal, strategy=depthfirst)
	costs_total = len(result) * u_cost

	print("init:\t\t", root)
	print("goal:\t\t", goal)
	print("result:\t\t")

	for r in result:
		for l in r._data:
			print(l)
		print("")

	print("")

	print("cost p/p:\t", u_cost)
	print("len:\t\t", len(result))
	print("costs:\t\t", costs_total)
	print("checked:\t", path_len)

	print("\n", "--" * 40, "\n")

	result, path_len = solve(root, goal, strategy=breadthfirst)
	costs_total = len(result) * u_cost

	print("init:\t\t", root)
	print("goal:\t\t", goal)
	print("result:\t\t")

	for r in result:
		for l in r._data:
			print(l)
		print("")

	print("")

	print("cost p/p:\t", u_cost)
	print("len:\t\t", len(result))
	print("costs:\t\t", costs_total)
	print("checked:\t", path_len)
