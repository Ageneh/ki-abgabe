from puzzle.a_star import AStar, h_manhattan, h_hamilton
from puzzle.node import Node
from puzzle.uninformed import depthfirst, Uninformed, breadthfirst


def print_result(solution, horiz=False):
    if not horiz:
        for r in solution:
            for l in r._data:
                print(l)
            print("")
    else:
        lines = {}
        last = len(solution) - 1
        for board in solution:
            for r in range(len(board)):
                if r not in lines: lines[r] = ""

                lines[r] += str(board[r])

                if solution.index(board) < last: lines[r] += "\t|\t"

        for l in sorted(lines.keys()): print(lines[l])

        print("")


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

    alg = AStar()
    result, path_len = alg.solve(root, goal, strategy=depthfirst, heuristic=h_hamilton)
    costs_total = len(result) * u_cost

    print("init:\t\t", root)
    print("goal:\t\t", goal)
    print("result:\t\t")

    print("")
    print_result(result, horiz=True)

    print("cost p/p:\t", u_cost)
    print("len:\t\t", len(result))
    print("costs:\t\t", costs_total)
    print("checked:\t", path_len)
