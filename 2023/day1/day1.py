with open('day1_input.txt') as calories:
    elf_calories = calories.readlines() # list of string elements

# list massage
elf_calories_grouped = "".join(elf_calories)

print(elf_calories_grouped)
