import itertools

with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2022\day1\day1_input.txt") as calories:
    elf_calories = [line.strip("\n") for line in calories]

# grouping
cal_groups = itertools.groupby(elf_calories, lambda sep: sep == "")

calories_grouped = [list(gr) for key, gr in cal_groups if not key]

# integers and sums
elf_cal_sums = [sum(list(map(int, i))) for i in calories_grouped]

# sort
elf_cal_sums.sort()

top_three_elfs = elf_cal_sums[-1] + sum(elf_cal_sums[-3: -1])

print(top_three_elfs)
