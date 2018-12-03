def print_result(solution, horiz=False):
    if not horiz:
        for row in solution:
            for col in row._data:
                print(col)
            print("")
    else:
        lines = {}
        last = len(solution) - 1
        for board in solution:
            for row in range(len(board)):
                if row not in lines: lines[row] = ""

                lines[row] += str(board[row])

                if solution.index(board) < last: lines[row] += "\t|\t"

        for col in sorted(lines.keys()): print(lines[col])

        return lines