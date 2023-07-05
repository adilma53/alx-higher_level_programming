#!/usr/bin/python3
"""
N QUEEN PROBLEMS
"""
from sys import argv


def check_spot(board, row, col):
    """
    Checks if a spot on the board is safe to place a queen.

    Args:
        board: The current state of the chessboard.
        row: The row index of the spot to be checked.
        col: The column index of the spot to be checked.

    Returns:
        1 if the spot is safe, 0 otherwise.
    """
    n = len(board) - 1

    if board[row][col]:
        return 0

    for r in range(row):
        if board[r][col]:
            return 0

    i = row
    j = col
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if board[i][j]:
            return 0

    i = row
    j = col
    while i > 0 and j < n:
        i -= 1
        j += 1
        if board[i][j]:
            return 0

    return 1


def init_board(n=4):
    """
    Initializes a chessboard of size n x n with zeros.

    Args:
        n: The size of the chessboard.

    Returns:
        A 2D list representing the chessboard.
    """
    board = []
    for r in range(n):
        board.append([0 for _ in range(n)])
    return board


def find_solution(board, row):
    """
    Finds a solution to the N-Queens problem using backtracking.

    Args:
        board: The current state of the chessboard.
        row: The current row to start searching for a safe spot.

    Returns:
        The solved board if a solution is found, None otherwise.
    """
    for col in range(len(board)):
        if check_spot(board, row, col):
            board[row][col] = 1
            if row == len(board) - 1:
                print(convert_to_solution(board))
                board[row][col] = 0
                continue
            if find_solution(board, row + 1):
                return board
            else:
                board[row][col] = 0
    return None


def convert_to_solution(board):
    """
    Converts the solved board to a list of queen positions.

    Args:
        board: The solved chessboard.

    Returns:
        A list of queen positions in the format [(row, col)].
    """
    solution = []
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c]:
                solution.append((r, c))
    return solution


def n_queens(n=4):
    """
    Finds and prints all solutions to the N-Queens problem.

    Args:
        n: The size of the chessboard.
    """
    for col in range(n):
        board = init_board(n)
        board[0][col] = 1
        find_solution(board, 1)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    n_queens(n)
