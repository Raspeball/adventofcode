# importing
import math
import numpy as np
#
#
#
# Reading input and formating

bingo_numbers_pool = []
raw_boards = []

with open("day4-input_custom.txt") as input_data:

    for line_num, line in enumerate(input_data):

        if line_num == 0:
            bingo_numbers_pool = list(map(int, line.split(',')))

        else:
            row = [int(num) for num in line.strip().split(" ") if num != ""]

            raw_boards.append(row)

        # removing empty lists caused by list comprehension syntax
        for ele in raw_boards:
            if ele == []:
                raw_boards.remove(ele)



# Further formating of bingo boards: list of list of lists
bingo_boards = []
for i in range(0, len(raw_boards), 5):
    curr_board = raw_boards[i:i+5]
    bingo_boards.append(curr_board)


### --- --- ###

def AddWinnerCounter(board_arr):

    for board in board_arr:
        for row in board:
            row.append(0)

        board.append([0,0,0,0,0])

#AddWinnerCounter(bingo_boards)

#print(bingo_boards)

def CheckBoard(board_arr, b): #works
    # b is a number, ie. a drawn bingo number

    row_win = False
    col_win = False
    winner_board = -1

    for board in board_arr:
        for row in board:
            if b in row:
                row[-1] -= 1
                board[-1][row.index(b)] -= 1
                if row[-1] == -5:
                    row_win = True
                    winner_board = board_arr.index(board)

                elif board[-1][row.index(b)] == -5:
                    col_win = True
                    winner_board = board_arr.index(board)


    return board_arr, winner_board


def PlayBingo(list_of_boards, nums):
    # list_of_boards is an array of boards, which is a list of rows
    # nums is a list of numbers to be drawn

    # initialize

    for n in nums:
        update_boards, win = CheckBoard(list_of_boards, n)
        if win != -1:
            break


    winner_board = list_of_boards[win]

    return winner_board


def CalculateScore(wboard):
    
