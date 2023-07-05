#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]

    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check for queens in the lower diagonal
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(N, board, row, solutions):
    # Solve the N queens problem using backtracking

    if row == N:
        # Found a solution
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(N, board, row + 1, solutions)
            board[row][col] = 0


def nqueens(N):
    # Solve the N queens problem and print the solutions

    # Check if N is an integer greater or equal to 4
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0] * N for _ in range(N)]
    solutions = []

    solve_nqueens(N, board, 0, solutions)

    # Print the solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
