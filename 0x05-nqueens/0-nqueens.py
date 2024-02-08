#!/usr/bin/python3
'''Module that includes nquens function
that prints all solution for N queens puzzle
'''


def nqueens(N):
    "Prints all solution for N queens puzzle"
    q = {n: None for n in range(N)}
    i = 0
    j = 0
    while i < N:
        while j < N:
            attack = False
            for queen in q.values():
                if queen:
                    if (queen[0] + queen[1]) == (i + j):
                        attack = True
                    if (queen[1] == j):
                        attack = True
                    if (i - queen[0]) == (j - queen[1]):
                        attack = True
            if not attack:
                q[i] = [i, j]
                j = 0
                break
            j += 1
        if i and not q[i] and q[i - 1]:
            j = q[i - 1][1] + 1
            q[i - 1] = None
            i -= 1
            continue
        i += 1
        if all(value is not None for value in q.values()):
            print(list(q.values()))
            j = q[0][1] + 1
            i = 0
            q = {n: None for n in range(N)}


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        try:
            N = int(sys.argv[1])
            if N < 4:
                print("N must be at least 4")
                exit(1)
            nqueens(N)
        except (ValueError, TypeError):
            print("N must be a number")
            exit(1)
    else:
        print("Usage: nqueens N")
        exit(1)
