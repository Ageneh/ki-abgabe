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
                string = "logs/log_{}_{}_{}.txt".format("a-star", strategy.__name__, datetime.now())
                file = open(string, "w")

            file.write("root: {}\n".format(start))
            file.write("goal: {}\n\n".format(goal))

        while queue:
            state = queue.pop(0)

            if log:
                file.write(str(i))
                file.write(" node:")
                file.write(str(state))
                file.write("\n")
                i += 1

            if is_depth and state.depth() >= max_depth: continue

            if log:
                file.write(str(i))
                file.write(" node:")
                file.write(str(state))
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

            reached.append(state)
            children = state.expand()
            newex = [s for s in children if s not in reached]

            queue = strategy(queue, newex)

        file.close()
        return None
