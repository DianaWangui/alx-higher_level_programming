#!/usr/bin/python3

"""Quuens puzzle challenge."""

import sys


def is_safe(board, row, col, n):
    """Check if there is a queen in the same col."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
               return False

    return True

def print_solution(board):
    n = len(board)
    for i in range(n):
        row = ["Q" if j == board[i] else "." for j in range(n)]
        print(" ".join(row))
    print()

def solve_nqueens(board, row, n):
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = 0 # Backtracking

def nqueens(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * n
    solve_nqueens(board, 0, n)
