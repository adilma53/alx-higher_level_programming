#!/usr/bin/python3
"""N QUEEN PROBLEM"""
from sys import argv


def checkspot(board, row, column):
    n = len(board) - 1
    if board[row][column]:
        return 0
    for r in range(row):
        if board[r][column]:
            return 0
    i = row
    j = column
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if board[i][j]:
            return 0
    i = row
    j = column
    while i > 0 and j < n:
        i -= 1
        j += 1
        if board[i][j]:
            return 0
    return 1


def initboard(n=4):
    b = []
    for row in range(n):
        b.append([0 for column in range(n)])
    return b


def findsoln(board, row):
    for column in range(len(board)):
        if checkspot(board, row, column):
            board[row][column] = 1
            if row == len(board) - 1:
                print(convtosoln(board))
                board[row][column] = 0
                continue
            if findsoln(board, row + 1):
                return board
            else:
                board[row][column] = 0
    return None


def convtosoln(board):
    soln = []
    n = len(board)
    for row in range(n):
        for column in range(n):
            if board[row][column]:
                soln.append([row, column])
    return soln


def nqueens(n=4):
    for column in range(n):
        board = initboard(n)
        board[0][column] = 1
        findsoln(board, 1)


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
    nqueens(n)
