'''
Codewards Kata: Is the King in check?
https://www.codewars.com/kata/5e28ae347036fa001a504bbe/train/python

5kyu

I solved this kata twuce but the  first time was horribly inefficient.
This is my second attampt with a better solution.

Previously I tried to check all the pieces on the board and see if they put the King in check.
This solution takes the King's position and sees if the appropriate pieces are
in the right spot to put the King in check.
'''

def king_is_in_check(chessboard):
    # KING SETUP
    king = '♔'
    for row, s in enumerate(chessboard):
        for col, i in enumerate(s):
            if i == king:
                king_row = row
                king_col = col
    # OTHER PIECES DEFINED
    pawn = '♟'
    knight = '♞'
    rook = '♜'
    bishop = '♝'
    queen = '♛' 
##### PAWN CHECK
    if king_col>0:
        if chessboard[king_row-1][king_col-1] == pawn:
            return True
    if king_col<7:
        if chessboard[king_row-1][king_col+1] == pawn:
            return True
##### KNIGHT CHECK
    # up
    if king_row > 1 and king_col>0:
        if chessboard[king_row-2][king_col-1] == knight:
            return True
    if king_row > 1 and king_col<7:
        if chessboard[king_row-2][king_col+1] == knight:
            return True
    # right
    if king_row > 0 and king_col < 6:
        if chessboard[king_row-1][king_col+2] == knight:
            return True
    if king_row < 7 and king_col < 6:
        if chessboard[king_row+1][king_col+2] == knight:
            return True
    # down
    if king_row < 6 and king_col <7:
        if chessboard[king_row+2][king_col+1] == knight:
            return True
    if king_row < 6 and king_col > 0:
        if  chessboard[king_row+2][king_col-1] == knight:
            return True
    # left
    if king_row < 7 and king_col > 1:
        if chessboard[king_row+1][king_col-2] == knight:
            return True
    if king_row > 0 and king_col > 1:
        if chessboard[king_row-1][king_col-2] == knight:
            return True
##### ROOK CHECK + QUEEN
    # left horizontal
    for n in range(king_col-1,-1,-1):
        if chessboard[king_row][n] == rook or chessboard[king_row][n] == queen:
            return True
        elif chessboard[king_row][n] != ' ':
            break
    # right horizontal
    for n in range(king_col+1,8):
        if chessboard[king_row][n] == rook or chessboard[king_row][n] == queen:
            return True
        elif chessboard[king_row][n] != ' ':
            break
    # up vertical
    for n in range(king_row-1,-1,-1):
        if chessboard[n][king_col] == rook or chessboard[n][king_col] == queen:
            return True
        elif chessboard[n][king_col] != ' ':
            break
    # down vertical
    for n in range(king_row+1,8):
        if chessboard[n][king_col] == rook or chessboard[n][king_col] == queen:
            return True
        elif chessboard[n][king_col] != ' ':
            break
##### BISHOP CHECK + QUEEN
    # up and right
    count = 1
    while True:
        if king_row-count < 0 or king_col+count > 7:
            break
        print([[king_row-count],[king_col+count]])
        if chessboard[king_row-count][king_col+count] == bishop or chessboard[king_row-count][king_col+count] == queen:
            return True
        elif chessboard[king_row-count][king_col+count] != ' ':
            break
        count += 1
    # down and right
    count = 1
    while True:
        if king_row+count > 7 or king_col+count > 7:
            break
        print([[king_row+count],[king_col+count]])
        if chessboard[king_row+count][king_col+count] == bishop or chessboard[king_row+count][king_col+count] == queen:
            return True
        elif chessboard[king_row+count][king_col+count] != ' ':
            break
        count += 1
    # down and left
    count = 1
    while True:
        if king_row+count > 7 or king_col-count < 0:
            break
        print([[king_row+count],[king_col-count]])
        if chessboard[king_row+count][king_col-count] == bishop or chessboard[king_row+count][king_col-count] == queen:
            return True
        elif chessboard[king_row+count][king_col-count] != ' ':
            break
        count += 1
    # up and left
    count = 1
    while True:
        if king_row-count < 0 or king_col-count < 0:
            break
        print([[king_row-count],[king_col-count]])
        if chessboard[king_row-count][king_col-count] == bishop or chessboard[king_row-count][king_col-count] == queen:
            return True
        elif chessboard[king_row-count][king_col-count] != ' ':
            break
        count += 1
### CHECK NOT FOUND
    return False