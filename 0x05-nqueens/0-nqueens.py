#!/usr/bin/python3
"""
nqueens problem
"""
import sys


def backtrack(row, n, cols, pos, neg, board):
    """
    backtrack function
    """
    if row == n:
        out = []
        for i in range(len(board)):
            for k in range(len(board[i])):
                if board[i][k] == 1:
                    out.append([i, k])
        print(out)
        return

    for col in range(n):
        if col in cols or (row + col) in pos or (row - col) in neg:
            continue

        cols.add(col)
        pos.add(row + col)
        neg.add(row - col)
        board[row][col] = 1

        backtrack(row+1, n, cols, pos, neg, board)

        cols.remove(col)
        pos.remove(row + col)
        neg.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Solution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(n[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
