import itertools

with open("day1_input.txt") as calories:
    elf_calories = [line for line in calories]

# grouping
cal_groups = itertools.groupby(elf_calories, lambda sep: sep == "\n")

elf_calories_grouped = [list(gr) for key, gr in cal_groups if not key]



print(elf_calories_grouped)
