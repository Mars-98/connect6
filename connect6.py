import numpy as np
from soupsieve.util import string

ROW_CNT = 8
COLUMN_CNT = 9


def createBoard():
    board = np.zeros((ROW_CNT, COLUMN_CNT), dtype=int)
    return board


board = createBoard()
print(board)
gameEnd = False
turn = 0


def dropPiece(Board, Row, Col, playerPiece):  # drop the piece in the spot the player has chosen
    Board[Row][Col] = playerPiece


def validLoc(Board, Col):  # checks if the position we chose is valid for input
    if Board[ROW_CNT - 1][Col] == 0:
        return True
    return False


def nextOpenRow(Board, Col):  # gets the next open row on the column we're on
    for Row in range(ROW_CNT):
        if Board[Row][Col] == 0:
            return Row


def changeTurn(Turn):
    Turn += 1  # increments to 1 for player 2's turn
    Turn %= 2  # maintains turn to stay between 0 and 1
    return Turn


def checkWin(Board):
    counter = 0
    # check for horizontal win
    for r in range(ROW_CNT - 1):
        for c in range(COLUMN_CNT - 5):  # range is exclusive, so it goes from 0 to (COLUMN_CNT-5)-1 == 3
            if Board[r][c] == Board[r][c + 1] == Board[r][c + 2] == Board[r][c + 3] == Board[r][c + 4] \
                    == Board[r][c + 5] != 0:
                return True

    # check for vertical win
    for c in range(COLUMN_CNT - 1):
        for r in range(ROW_CNT - 5):  # range is exclusive, so it goes from 0 to (R0W_CNT-5)-1 == 2
            if Board[r][c] == Board[r + 1][c] == Board[r + 2][c] == Board[r + 3][c] == Board[r + 4][c] \
                    == Board[r + 5][c] != 0:
                return True

    # check for + slope diagonal win
    for c in range(COLUMN_CNT - 5):  # range is exclusive, so it goes from 0 to (COLUMN_CNT-5)-1 == 3
        for r in range(ROW_CNT - 5):  # range is exclusive, so it goes from 0 to (R0W_CNT-5)-1 == 2
            if Board[r][c] == Board[r + 1][c + 1] == Board[r + 2][c + 2] == Board[r + 3][c + 3] == Board[r + 4][c + 4] \
                    == Board[r + 5][c + 5] != 0:
                return True

    # check for - slope diagonal win
    for c in range(COLUMN_CNT - 5):  # range is exclusive, so it goes from 0 to (COLUMN_CNT-5)-8=1 == 3
        for r in range(5, ROW_CNT):  # starts at 5 and goes until ROW_CNT - 1
            if Board[r][c] == Board[r - 1][c + 1] == Board[r - 2][c + 2] == Board[r - 3][c + 3] == Board[r - 4][c + 4] \
                    == Board[r - 5][c + 5] != 0:  # wont need to check != 0 because the element it starts at wont be 0
                return True

    return False


def printBoard(Board):  # the axis of the board is row 1 column one, so pieces fill downward, so I flipped it and
    # assigned it a new axis on row
    print(np.flip(Board, 0))


# name1 = input("Lets get started! What's your name? ")
# name2 = input("Lets get started! What's your name? ")

while not gameEnd:

    # player one
    if turn == 0:
        player = string(1)  # casted to string bc I can't concatenate string and int inside of user input call
    # player two
    else:
        player = string(2)

    turn = changeTurn(turn)
    col = int(input("Player_" + player + ": select which position you want to fill: 0-8:  "))
    if validLoc(board, col):
        row = nextOpenRow(board, col)
        dropPiece(board, row, col, player)
    printBoard(board)
    if checkWin(board):
        print("Wow! Player " + player + " YOU WON!")
        gameEnd = True
