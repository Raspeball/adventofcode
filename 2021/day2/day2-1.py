# Reading input and formating

with open("day2-input.txt") as pos:
    instructions = [line.rstrip().split(" ") for line in pos]

for ele in instructions:
    ele[1] = float(ele[1])

# Defining functions that read positions from instructions list

def ReadInstructions(list):

    depth = 0
    horizontal_pos = 0

    for inst in list:
        if inst[0] == "up":
            depth = depth - inst[1]

        elif inst[0] == "down":
            depth += inst[1]

        else:
            if inst[0] == "forward":
                horizontal_pos += inst[1]

            else:
                continue

    return depth*horizontal_pos

def main():

    print(ReadInstructions(instructions))


if __name__ == "__main__":
    main()
