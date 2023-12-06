# Imports
import time

# Input day 5
day5_input = [[41, 214], [96, 1789], [88, 1127], [94, 1055]]# [[time, distance]]
day5_input_p2 = [41968894, 214178911271055]
#
#
def CalcDist(t0, hold):
    v = hold
    t = t0 - hold
    d = v*t

    return d

def IsRecordBeat(race_data):
    # race_data is a length 2 list [time, distance]
    # where time is avaliable time
    # and distance is the distance to beat
    avaliable_time, record_dist = [i for i in race_data]

    t0_start = record_dist // avaliable_time

    ways_to_beat = 0

    for h in range(t0_start, avaliable_time):
        if CalcDist(avaliable_time, h) > record_dist:
            ways_to_beat += 1
    
    return ways_to_beat

def main():
    ### --- Part 1 --- ###
    #sol = 1
    #
    #for race_stats in day5_input:
    #    sol = sol*IsRecordBeat(race_stats)
    #
    ### --- --- ###

    ### --- Part 2 --- ###
    start = time.time()
    sol = IsRecordBeat(day5_input_p2)
    end = time.time()
    print(sol)
    print(f"Execution time (ms): {(end-start)*10**3}")
##
#
# run  program
if __name__ == '__main__':
    main()

