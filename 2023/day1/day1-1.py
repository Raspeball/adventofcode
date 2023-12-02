with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2023\day1\day1_input.txt") as calibdata:
    caliblines = [line.strip("\n") for line in calibdata]

#temp = caliblines[0:5]
#print(temp)


def GetCalibVals(line):
    nums = [str(i) for i in range(10)]
    spelled_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    val1 = ""
    val2 = ""

    for i in line:
        if i in nums:
            val1 = i
            break
    
    for j in reversed(line):
        if j in nums:
            val2 = j
            break
    
    val = int(val1 + val2)
    
    return val


def SumOfCalibVals(data):
    # data is list of lines

    res = 0
    
    for line in data:
        res += GetCalibVals(line)
    
    return res

sol = SumOfCalibVals(caliblines)
print(sol)