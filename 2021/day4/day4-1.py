# importing
import math
import numpy as np
#
#
#
# Reading input and formating

bingo_numbers_pool = []
raw_boards = []

with open("day4-input.txt") as input_data:

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


def AddWinnerCounter(board_arr):

    for board in board_arr:
        for row in board:
            row.append(-1)

        board.append([-1,-1,-1,-1,-1])

    return board_arr

the_bingo_boards = AddWinnerCounter(bingo_boards) #final formating

#print(bingo_numbers_pool)
#print(bingo_numbers_pool[0:bingo_numbers_pool.index(24)])

### --- --- ###
def CheckBoard(board_arr, b): #works
    # b is a number, ie. a drawn bingo number

    row_col_win = False
    #row_win = False
    #col_win = False
    winner_board = -1

    for board in board_arr:
        for row in board:
            if b in row:
                row[-1] -= 1
                board[-1][row.index(b)] -= 1
                if row[-1] == -6 or board[-1][row.index(b)] == -6:
                    row_col_win = True
                    winner_board = board_arr.index(board)
                    break
            else:
                continue

                #elif board[-1][row.index(b)] == -6:
                #    col_win = True
                #    winner_board = board_arr.index(board)


    return board_arr, winner_board


def PlayBingo(list_of_boards, nums):
    # list_of_boards is an array of boards, which is a list of rows
    # nums is a list of numbers to be drawn

    # initialize

    for n in nums:
        list_of_boards, win = CheckBoard(list_of_boards, n)
        if win != -1:
            win_num = n
            break


    winner_board = list_of_boards[win]

    return winner_board, win_num


def FinalScore(wboard, wnum, bingo_nums):
    # this is a poor solution

    boardnums = []
    for row in wboard:
        for ele in row:
            if ele >= 0:
                boardnums.append(ele)

    drawn = bingo_nums[0:bingo_nums.index(wnum) + 1]
    unmarked = [n for n in boardnums if n not in drawn]
    #print(drawn)

    res = sum(unmarked)
    #print(res)

    final_score = res*wnum

    return final_score




#
#
#
def main():
    # calling PlayBingo to run the bingo
    the_winner_board, the_winner_num = PlayBingo(the_bingo_boards, bingo_numbers_pool)

    #printing for manual purposes
    print(the_winner_board)
    print(the_winner_num)

    the_final_score = FinalScore(the_winner_board, the_winner_num, bingo_numbers_pool)
    print(the_final_score)

# run program
if __name__ == "__main__":
    main()

# testing
# nums are 53 and 68
#res, y = CheckBoard(the_bingo_boards, 53)
#print(res)

#res2, y = CheckBoard(res, 68)
#print(res2)
