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
	def solve(start, goal, heuristic=h_manhattan, **kwargs):
		p_queue = [(0, start)]  # [(dist + heuristic_val, node), ...]
		reached = [start]
		costs_nodes = {start: 0}  # total costs to each node
		i = 1

		while p_queue:
			cost, state = p_queue.pop(0)

			i += 1

			if state == goal:
				return state.path(), i

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

		return None
