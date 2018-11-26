from puzzle.node import Node


_max_depth = 50


def breadthfirst(queue, expanded, **kargs):
	for e in expanded:
		queue.append(e)
	return queue


def depthfirst(stack, expanded, depth=1, max_depth=_max_depth):
	if depth < max_depth:
		for e in expanded:
			stack.insert(0, e)
	else:
		return breadthfirst(stack, expanded)
	return stack


def solve(start, goal, strategy=breadthfirst):
	queue = [start]
	reached = [start]
	depth = 0

	while queue:
		state = queue.pop(0)
		if state == goal:

			path = [state]
			while hasattr(path[-1], "_parent"):
				path.append(path[-1].parent())

			return path[::-1], len(reached)

		# print(state)

		reached.append(state)
		children = state.expand()
		depth += 1
		newex = [s for s in children if s not in reached]
		# newex = []
		# for s in children:
		# 	if s not in reached:
		# 		newex.append(s)

		# queue = strategy(queue, newex)
		queue = strategy(queue, newex, depth=depth, max_depth=40)

		# for s in newex:
		# 	queue.append(s)

		if len(reached) % 300 == 0:
			print("len:", len(reached), ",", "dep:", depth, "# # "*30, "\n")

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
	costs_total = path_len * u_cost

	print("init:\t\t", root)
	print("goal:\t\t", goal)
	print("result:\t\t", result)
	print("cost p/p:\t", u_cost)
	print("path len:\t", path_len)
	print("costs:\t\t", costs_total)
