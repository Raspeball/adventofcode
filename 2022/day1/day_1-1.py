import itertools

with open("day1_input.txt") as calories:
    elf_calories = [line.strip("\n") for line in calories]

# grouping
cal_groups = itertools.groupby(elf_calories, lambda sep: sep == "")

calories_grouped = [list(gr) for key, gr in cal_groups if not key]

# integers and sums
elf_cal_sums = [sum(list(map(int, i))) for i in calories_grouped]

cal_max = max(elf_cal_sums)
elf = elf_cal_sums.index(cal_max)

print(cal_max, elf)

