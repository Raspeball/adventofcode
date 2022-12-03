## Advent of Code 2022: Day 3 ##
# https://adventofcode.com/2022/day/3 #
#

# read day3 data
with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2022\day3-input.txt") as data:
    rucksacks = [line.strip("\n") for line in data]

# define priorities
lower_alph = "abcdefghijklmnopqrstuvwxyz"
priority_alph = lower_alph + lower_alph.upper()

# find commmon items
def CommonItemRucksack(content):
    comp_lim = int(len(content)/2)
    comps = [content[0: comp_lim], content[comp_lim: int(len(content))]]

    for i in comps[0]:
        if i in comps[1]:
            return i

# sum priorities
def CalcPriority(content):

    pri = priority_alph.index(CommonItemRucksack(content)) + 1

    return pri

# main
def main():

    sum_of_pri_common = 0

    for ruck in rucksacks:
        sum_of_pri_common += CalcPriority(ruck)
    
    print(f"Sum of priorities: {sum_of_pri_common}")

# run program
if __name__ == "__main__":
    main()

