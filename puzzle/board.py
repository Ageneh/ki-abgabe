from puzzle.node import Node


def solve(start, goal):
	queue = [start]
	reached = [start]

	while queue:
		state = queue.pop(0)
		if state == goal:
			return state, len(reached)

		reached.append(state)
		children = state.expand()
		newex = [s for s in children if s not in reached]
		# newex = []
		# for s in children:
		# 	if s not in reached:
		# 		newex.append(s)

		for s in newex:
			queue.append(s)

		if len(reached) % 300 == 0:
			print("len:", len(reached), ",", "# # "*30, "\n")

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

	result, path_len = solve(root, goal)
	costs_total = path_len * u_cost

	print("init:\t\t", root)
	print("goal:\t\t", goal)
	print("cost p/p:\t", u_cost)
	print("path len:\t", path_len)
	print("costs:\t\t", costs_total)
