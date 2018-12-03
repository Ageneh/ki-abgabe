from puzzle import print_result

def h_hamilton(node, goal):
	sum = 0
	for y in range(len(node)):
		for x in range(len(node[y])):
			sum += goal[y][x] != node[y][x]
	return sum


def h_manhattan(node, goal):
	sum = 0
	for y in range(len(node)):
		for x in range(len(node[y])):
			g_x, g_y = goal.get_pos(val=node[y][x])
			sum += abs(y - g_y) + abs(x - g_x)
	return sum


class AStar:

	@staticmethod
	def solve(start, goal, heuristic=h_manhattan, log=False, log_file=None, w_costs=1, **kwargs):
		from datetime import datetime
		p_queue = [(0, start)]
		reached = [start]
		costs_nodes = {start: 0}  # total costs to each node
		i = 1
		file = None
		if log:
			if log_file:
				file = open(log_file, "w")
			else:
				string = "logs/log_{}_{}_{}.txt".format("a-star", heuristic.__name__, datetime.now())
				file = open(string, "w")

			file.write("root: {}\n".format(start))
			file.write("goal: {}\n\n".format(goal))

		while p_queue:
			cost, state = p_queue.pop(0)

			if log:
				file.write(str(i))
				file.write(" node:")
				file.write(str(state))
				file.write("; ")
				file.write("costs:")
				file.write(str(costs_nodes[state]))
				file.write("\n")
				i += 1

			if state == goal:
				path = state.path()

				if log:
					file.write("\nresult:\n")
					lines = print_result(state.path(), horiz=True)
					for l in sorted(lines.keys()):
						file.write(lines[l])
						file.write("\n")
					file.write("\npath length:\t")
					file.write(str(len(path)))
					file.write("\n")

					file.close()

				return path, len(reached)

			print("node:", state)

			reached.append(state)
			children = state.expand()

			for child in children:
				cost_to_child = costs_nodes[state] + child.cost()
				heuristic_val = heuristic(child, goal)
				n_cost = cost_to_child + heuristic_val
				if child not in costs_nodes or n_cost < costs_nodes[child]:
					costs_nodes[child] = cost_to_child
					child.set_total_cost(cost_to_child)
					p_queue.append((n_cost, child))

			p_queue = sorted(p_queue, key=lambda x: x[0])

		file.close()

		return None
