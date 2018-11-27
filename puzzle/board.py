_max_depth = 7


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
	while path[-1].parent() and not path[-1].is_root():
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
