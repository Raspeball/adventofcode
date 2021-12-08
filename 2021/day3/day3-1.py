# importing
import math
#
#
#
# Reading input and formating

with open("day3-input.txt") as nums:
    diagnostics = [line.rstrip() for line in nums]

#
#
# Define functions
#
def MostCommonBit(list):
    # list is the diagnostics list consisting of string elements
    # which are strings of 0 and 1

    most_common = ""
    least_common = ""
    length = len(list[0]) # assume all elements are of equal lenths

    for i in range(length):
        ones = 0
        zeroes = 0
        for ele in list:
            if ele[i] == "0":
                zeroes += 1

            else:
                ones += 1
        #print(f"Ones: {ones} and Zeros: {zeroes}")
        if ones > zeroes:
            most_common += "1"
            least_common += "0"
        else:
            most_common += "0"
            least_common += "1"

    return [most_common, least_common]

#
#
def main():

    gamma = int(MostCommonBit(diagnostics)[0], 2)
    epsilon = int(MostCommonBit(diagnostics)[1], 2)

    print(f"Gamma = {gamma}; Epsilon = {epsilon}")

    power_consumption = gamma*epsilon

    print(f"The power consumption is {power_consumption}")
#
#
# run program
if __name__ == "__main__":
    main()
