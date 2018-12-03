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
    def solve(start, goal, heuristic=h_manhattan, w_costs=1, **kwargs):
        p_queue = [(0, start)]
        reached = [start]
        current_costs = {start: 0} # total costs to each node


        while p_queue:
            cost, state = p_queue.pop(0)

            if state == goal:
                return state.path(), len(reached)

            reached.append(state)
            children = state.expand()

            for child in children:
                n_cost = current_costs[state] + w_costs
                if child not in current_costs or n_cost < current_costs[child]:
                    current_costs[child] = n_cost
                    prio = n_cost + heuristic(child, goal)
                    p_queue.append((prio, child))

            p_queue = sorted(p_queue, key=lambda x: x[0])

        return None
