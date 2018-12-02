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
	def solve(start, goal, heuristic=h_manhattan, **args):
		p_queue = [(0, start)]
		reached = [start]

		while p_queue:
			cost, state = p_queue.pop(0)

			if state == goal:
				return state.path(), len(reached)

			reached.append(state)
			children = state.expand()
			newex = [(cost + heuristic(s, goal), s) for s in children if s not in reached]
			p_queue.extend(newex)
			p_queue = sorted(p_queue, key=lambda x: x[0])

		return None
