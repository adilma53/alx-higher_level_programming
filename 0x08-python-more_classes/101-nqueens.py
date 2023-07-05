#!/usr/bin/python3
"""the N queens problem"""
import sys


def is_valid(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # If there are no conflicts, the move is valid
    return True


def solve_n_queens(n):
    board = [[0 for i in range(n)] for j in range(n)]
    solutions = []
    solve_n_queens_helper(n, board, 0, solutions)
    return solutions


def solve_n_queens_helper(n, board, row, solutions):
    # If we've placed all the queens, we've found a solution
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_helper(n, board, row + 1, solutions)
            board[row][col] = 0


def main():
    # Parse command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the problem and print the solutions
    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
