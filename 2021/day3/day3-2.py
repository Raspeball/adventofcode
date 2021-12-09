# importing
import math
#
#
#
# Reading input and formating

with open("day3-input.txt") as nums:
    diagnostics = [line.rstrip() for line in nums]

# testing with values from day 3 example
#diagnostics = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
#
#
# Define functions
#
def MostCommonBit(list, pos):
    # list is the diagnostics list consisting of string elements
    # which are strings of 0 and 1


    most_common = ""
    least_common = ""
    ones = 0
    zeroes = 0

    for ele in list:
        if ele[pos] == "0":
            zeroes += 1

        else:
            ones += 1

    if ones > zeroes or ones == zeroes:
        most_common = "1"
        least_common = "0"


    else:
        most_common = "0"
        least_common = "1"

    return [most_common, least_common]


def KeepMostCommon(list, mc, pos):
    # mc = most common;
    # pos is the position in the string/bit
    # i.e in the string "101001", pos = 2 has value 1
    # pos = 0 has alså value 1
    if len(list) > 1:
        mc_rating = [ele for ele in list if ele[pos] == str(mc)]

    else:
        mc_rating = list

    return mc_rating

def KeepLeastCommon(list, lc, pos):
    # lc = least common
    # pos is the position in the string/bit
    # i.e in the string "101001", pos = 2 has value 1
    # pos = 0 has alså value 1
    if len(list) > 1:
        lc_rating = [ele for ele in list if ele[pos] == str(lc)]

    else:
        lc_rating = list

    return lc_rating


#
#
def main():

    # need copies of diagnostics
    OG_rate = diagnostics
    CO2_rate = diagnostics


    for i in range(len(diagnostics[0])):
        # this is the position

        # Get most and least common bit
        most = MostCommonBit(OG_rate, i)[0]
        least = MostCommonBit(CO2_rate, i)[1]

        # Keep only the bit-strings with most and least common
        OG_rate = KeepMostCommon(OG_rate, most, i)
        CO2_rate = KeepLeastCommon(CO2_rate, least, i)

    # Printing for testing purposes #
    #print(OG_rate)
    #print(CO2_rate)

    # Calculate the product
    oxygen = int(OG_rate[0], 2)
    co2 = int(CO2_rate[0], 2)
    life_support_rating = oxygen*co2

    print(f"The life support rating is {life_support_rating}")

#
#
# run program
if __name__ == "__main__":
    main()
