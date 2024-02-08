#!/usr/bin/python3
'''Module that includes nquens function
that prints all solution for N queens puzzle
'''


def nqueens(N):
    "Prints all solution for N queens puzzle"
    queens = {n: None for n in range(N)}
    row = 0
    col = 0
    while row < N:
        while col < N:
            attack = False
            for queen in queens.values():
                if queen:
                    queen_row, queen_col = queen
                    if (queen_col == col):
                        attack = True
                    if abs(row - queen_row) == abs(col - queen_col):
                        attack = True
            if not attack:
                queens[row] = [row, col]
                col = 0
                break
            col += 1
        if row and not queens[row] and queens[row - 1]:
            col = queens[row - 1][1] + 1
            queens[row - 1] = None
            row -= 1
            continue
        row += 1
        if all(value is not None for value in queens.values()):
            print(list(queens.values()))
            col = queens[0][1] + 1
            row = 0
            queens = {n: None for n in range(N)}


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        try:
            N = int(sys.argv[1])
            if N < 4:
                print("N must be at least 4")
                exit(1)
            nqueens(N)
        except ValueError:
            print("N must be a number")
            exit(1)
    else:
        print("Usage: nqueens N")
        exit(1)
