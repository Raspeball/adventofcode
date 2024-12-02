#
#
# open puzzle input
with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2024\day1\day1_input.txt") as puzzle_input:
    location_ids = [line.split() for line in puzzle_input]
#
#
# sorting of location ids
def sort_location_ids(loc_ids):
    left = [int(loc_pair[0]) for loc_pair in loc_ids]
    right = [int(loc_pair[1]) for loc_pair in loc_ids]

    right.sort()
    left.sort()

    return [left, right]
#
#
# calculate the toatal distance of the location ids
def calculate_location_dist(loc_ids):
    tot_dist = 0

    for p in range(len(loc_ids[0])):
        tot_dist += abs(loc_ids[0][p] - loc_ids[1][p])

    return tot_dist
#
#
def calculate_sim_score(loc_ids):
    tot_sim_score = 0

    left, right = loc_ids[0], loc_ids[1]

    for lid in left:
        tot_sim_score += lid*(right.count(lid))
    
    return tot_sim_score
#
#
# main
def main():
    data = sort_location_ids(location_ids)
    #res1 = calculate_location_dist(data)
    res2 = calculate_sim_score(data)
    
    print(res2)
#
#
# run program #
if __name__ == '__main__':
    main()


