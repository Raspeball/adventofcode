## Advent of Code 2022: Day 3 ##
# https://adventofcode.com/2022/day/3 #
#

# read day3 data
with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2022\day3-input.txt") as data:
    rucksacks = [line.strip("\n") for line in data]

### --- Part one --- ###

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

# calculate priorities
def CalcPriority(content):

    pri = priority_alph.index(CommonItemRucksack(content)) + 1

    return pri

### --- --- ###

### --- Part two --- ###

# find and calculate the badge priority
def FindBadgePri(elf_group):
    # elf group is a list of lenght 3
    for letter in elf_group[0]:
        if letter in elf_group[1] and letter in elf_group[2]:
            return priority_alph.index(letter) + 1
    #

# group elf rucksacks
def ElfGrouping(sacks):
    # sacks is the data from input
    groups = []
    
    for i in range(0, len(sacks), 3):
        groups.append(sacks[i: i+3])
    
    return groups

### --- --- ###

### --- --- ###
# main
def main():

    # Part one
    sum_of_pri_common = 0

    for ruck in rucksacks:
        sum_of_pri_common += CalcPriority(ruck)
    
    print(f"Sum of priorities: {sum_of_pri_common}")

    # Part two
    sum_of_group_badge = 0
    elf_groups = ElfGrouping(rucksacks)

    for gr in elf_groups:
        sum_of_group_badge += FindBadgePri(gr)
    
    print(f"Sum of group badges: {sum_of_group_badge}")

# run program
if __name__ == "__main__":
    main()

