## Advent of Code 2022: Day 10 ##
# https://adventofcode.com/2022/day/10 #
#

# read day 10 data
# program elements are strings
with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2022\day10\day10-input.txt") as data:
    program = [line.strip("\n") for line in data]

count = 0 # global

# register reg,
# sum s
def Cycle():
    global count

    cycle_checks = [20 + 40*i for i in range(6)]
    
    count += 1
    
    if count in cycle_checks:
        return True
    else:
        return False


def main():

    x = 1
    ss_sum = 0 # signal strenght sum

    for inst in program:
        if inst == "noop":
            if Cycle():
                ss_sum += count*x
        
        else:
            add = int(inst[5: ])
            if Cycle():
                ss_sum += count*x
            if Cycle():
                ss_sum += count*x
            x += add
        
    print(ss_sum)

# run program
if __name__ == "__main__":
    main()

