from puzzle import print_result
from puzzle.a_star import AStar, h_manhattan, h_hamilton
from puzzle.node import Node
from puzzle.uninformed import depthfirst, Uninformed, breadthfirst


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

    alg = Uninformed()
    result, path_len = alg.solve(root, goal, strategy=breadthfirst, heuristic=h_hamilton, log=True)
    costs_total = len(result) * u_cost

    print("init:\t\t", root)
    print("goal:\t\t", goal)
    print("result:\t\t")

    print("")
    print_result(result, horiz=True)

    print("cost p/p:\t", u_cost)
    print("len:\t\t", len(result))
    print("costs:\t\t", result[-1].total_cost() * u_cost)
    print("checked:\t", path_len)
