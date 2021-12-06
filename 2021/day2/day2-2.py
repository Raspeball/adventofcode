# Reading input and formating

with open("day2-input.txt") as pos:
    instructions = [line.rstrip().split(" ") for line in pos]

for ele in instructions:
    ele[1] = float(ele[1])

# Testing
#test = instructions[0:4]

# Defining functions that read positions from instructions list

def ReadInstructions(list):

    depth = 0
    horizontal_pos = 0
    aim = 0

    for inst in list:
        if inst[0] == "up":
            #depth = depth - inst[1]
            aim = aim - inst[1]

        elif inst[0] == "down":
            #depth += inst[1]
            aim += inst[1]

        elif inst[0] == "forward":
            horizontal_pos += inst[1]
            depth = depth + (aim*inst[1])

    return depth*horizontal_pos

def main():

    #print(test)
    print(ReadInstructions(instructions))


if __name__ == "__main__":
    main()
