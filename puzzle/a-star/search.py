from puzzle import Node

_max_depth = 7


def path(node, reversed=False):
	path = [node]
	while path[-1].parent() and not path[-1].is_root():
		path.append(path[-1].parent())
	return path[::-1] if not reversed else path


def solve_a_star(start, goal):
	queue = [(0, start)]
	reached = [start]

	while queue:
		cost, state = queue.pop(0)

		# if state.depth() >= 6: continue

		if state == goal:
			return path(state), len(reached)

		reached.append(state)
		children = state.expand()
		newex = [(cost+1, s) for s in children if s not in reached]
		queue.extend(newex)
		queue = sorted(queue, key=lambda x: x[0])

	return None



def print_result(solution):
	for r in result:
		for l in r._data:
			print(l)
		print("")


if __name__ == '__main__':

	u_cost = 1

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

	root = Node(init, root=True)
	goal = Node(final, goal=True)

	result, path_len = solve_a_star(root, goal)
	costs_total = len(result) * u_cost

	print("init:\t\t", root)
	print("goal:\t\t", goal)
	print("result:\t\t")

	print("")
	print_result(result)

	print("cost p/p:\t", u_cost)
	print("len:\t\t", len(result))
	print("costs:\t\t", costs_total)
	print("checked:\t", path_len)