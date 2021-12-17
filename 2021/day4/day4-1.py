# importing
import math
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
