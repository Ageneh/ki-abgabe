def breadthfirst(queue, expanded):
	for e in expanded:
		queue.append(e)
	return queue


def depthfirst(stack, expanded):
	for e in expanded:
		stack.insert(0, e)
	return stack


class Universal:

	@staticmethod
	def solve(start, goal, strategy=breadthfirst, max_depth=6, **args):
		queue = [start]
		reached = [start]

		while queue:
			state = queue.pop(0)

			if state.depth() >= max_depth: continue

			if state == goal:
				return state.path(), len(reached)

			reached.append(state)
			children = state.expand()
			newex = [s for s in children if s not in reached]

			queue = strategy(queue, newex)

		return None

