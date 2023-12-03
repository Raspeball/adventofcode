#
with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2023\day1\day1_input.txt") as calibdata:
    caliblines = [line.strip("\n") for line in calibdata]


### --- Part 1 --- ###
#
#
def GetCalibVals(line):
    nums = [str(i) for i in range(1,10)]
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


### --- Part two --- ###
#
#
def ModifyCalibLine(data):
    # data is list of lines
    mod_data =  []
    
    nums = [str(i) for i in range(1, 10)]
    spelled_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    num_dic = dict(zip(nums, spelled_nums))

    for line in data:
        
        new_line = line
        for num in num_dic.keys():
            new_line = new_line.replace(num, num_dic[num])
        mod_data.append(new_line)

    return mod_data


def GetModCalibVals(line):
    # line is a string element of a list

    # reversed string/line
    rev_line = line[::-1]

    spelled_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    # dics that hold the position of spelled numbers in the line
    # find() returns -1 if a word is not in the string, and thus we don't need these
    num_pos = {spelled:line.find(spelled) for spelled in spelled_nums if line.find(spelled) != -1}
    num_pos_reverse = {spelled[::-1]:rev_line.find(spelled[::-1]) for spelled in spelled_nums if rev_line.find(spelled[::-1]) != -1}

    
    # sorting
    sorted_num_pos = dict(sorted(num_pos.items(), key=lambda item: item[1]))
    sorted_num_pos_reverse = dict(sorted(num_pos_reverse.items(), key=lambda item: item[1]))

    low = spelled_nums.index([k for k in sorted_num_pos.keys()][0]) + 1
    rev_low = spelled_nums.index([k for k in sorted_num_pos_reverse.keys()][0][::-1]) + 1

    return int(str(low) + str(rev_low))


def ModifiedSumOfCalibVals(data):
    # data is list of lines

    res = 0
    
    for line in ModifyCalibLine(data):
        res += GetModCalibVals(line)
    
    return res

# Part 1 output #
#sol = SumOfCalibVals(caliblines)
#print(sol)

# Part 2 output #
sol = ModifiedSumOfCalibVals(caliblines)
print(sol)