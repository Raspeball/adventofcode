## Advent of Code 2022: Day 4 ##
# https://adventofcode.com/2022/day/4 #
#

# read and format day4 data
with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2022\day4\day4-input.txt") as data:
    section_ids = [(pair.strip("\n")).split(",") for pair in data]
    section_ids[:] = [(list(id.split("-") for id in ele)) for ele in section_ids]
    section_ids[:] = [ele[0] + ele[1] for ele in section_ids]

##

### --- Part one --- ###

def GetPairRanges(pair_data):
    pair_ranges = []

    for pair in pair_data:
        id1 = range(int(pair[0]), int(pair[1]) + 1)
        id2 = range(int(pair[2]), int(pair[-1]) + 1)

        pair_ranges.append([id1, id2])
    
    return pair_ranges

def IsFullyContained(pair_range):
    # pair_range is a list of lenght 2,
    # where each element is a range (list of numbers)
    # i.e [[1, 8], [24, 91]]

    if len(pair_range[0]) >= len(pair_range[1]):
        return set(pair_range[1]).issubset(set(pair_range[0]))
    else:
        return set(pair_range[0]).issubset(set(pair_range[1]))

### --- --- ###

### --- Part two --- ###

def IsAnyOverLap(pair_range):
    # pair_range is a list of lenght 2,
    # where each element is a range (list of numbers)
    # i.e [[1, 8], [24, 91]]
    # returns False if there is overlap
    # returns True if there is NO overlap
    return set(pair_range[0]).isdisjoint(set(pair_range[1]))

### --- --- ###

# main
def main():
    full_range_ids = GetPairRanges(section_ids)

    fully_contained = 0
    any_overlap = 0

    for pair in full_range_ids:
        if IsFullyContained(pair):
            fully_contained += 1
        
        if not IsAnyOverLap(pair):
            any_overlap += 1
    
    print(f"Assignment pairs that are fully contained: {fully_contained}")
    print(f"Assignment pairs that have any overlap: {any_overlap}")


# run program
if __name__ == "__main__":
    main()