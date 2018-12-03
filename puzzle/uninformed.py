from puzzle import print_result


def breadthfirst(queue, expanded):
	for e in expanded:
		queue.append(e)
	return queue


def depthfirst(stack, expanded):
	for e in expanded:
		stack.insert(0, e)
	return stack


class Uninformed:

	@staticmethod
	def solve(start, goal, strategy=breadthfirst, max_depth=6, log=False, log_file=None, **kwargs):
		from datetime import datetime

		queue = [start]
		reached = [start]
		is_depth = strategy is depthfirst
		i = 0
		file = None
		if log:
			if log_file:
				file = open(log_file, "w")
			else:
				string = "logs/log_{}_{}_{}.txt".format("uninformed", strategy.__name__, datetime.now())
				file = open(string, "w")

			file.write("root: {}\n".format(start))
			file.write("goal: {}\n\n".format(goal))

		while queue:
			state = queue.pop(0)

			if log:
				file.write(str(i))
				file.write(" node: \t")
				file.write(str(state))
				file.write("\n")
				i += 1

			if is_depth and state.depth() >= max_depth: continue

			if state == goal:
				if log:
					file.write("\nresult:\n")
					lines = print_result(state.path(), horiz=True)
					file.write(lines)
					file.write("\n")
					file.write("\nchecked nodes:\t")
					file.write(str(len(reached)))
					file.write("\npath length:\t")
					file.write(str(len(state.path())))
					file.write("\n")
					file.write("total costs:\t")
					file.write(str(state.total_cost()))
					file.write("\n")

					file.close()

					return state.path(), len(reached)

			reached.append(state)
			children = state.expand()
			newex = [s for s in children if s not in reached]

			if log:
				for n in newex:
					n.set_total_cost(state.total_cost() + n.cost())

			queue = strategy(queue, newex)

		file.close()
		return None
