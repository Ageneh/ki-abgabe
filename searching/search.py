def sleep():
	from time import sleep
	sleep(0.05)


def breadthfirst(queue, expanded):
	for e in expanded:
		queue.append(e)
	return queue


def depthfirst(stack, expanded):
	for e in expanded:
		stack.insert(0, e)
	return stack


def search(start, goal, strategy=breadthfirst, desc=False, v=False):
	queue = [start]
	reached = [start]

	while queue:
		state = queue.pop(0)

		if state is goal:
			if v: print("goal:", state, "\t>\tnewex:", state.children())
			return state

		reached.append(state)
		children = state.expand()
		newex = [s for s in children if s not in reached]
		queue = sorted(strategy(queue, newex), key=lambda x: x.key(), reverse=desc)

		if v:
			print("state:", state, "\t>\tnewex:", newex, "\t>\tchildren:", state.children())
			sleep()

	return None
