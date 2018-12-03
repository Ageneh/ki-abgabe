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

        string = "\n".join([lines[l] for l in sorted(lines.keys())])

        # for l in sorted(lines.keys()): print(lines[l])
        print(string)

    return string