from puzzle.board import solve, depthfirst, breadthfirst, path
from puzzle.node import Node


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

	result, path_len = solve(root, goal, strategy=depthfirst)
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
