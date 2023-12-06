# Imports
import time
import numpy as np

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

    #t0_start = record_dist // avaliable_time #suboptimal??
    if avaliable_time**2 < 4*record_dist:
        raise Exception("No solutions")
    else:
        discr_root = np.sqrt(avaliable_time**2 - 4*record_dist)
        low = np.ceil(0.5*(avaliable_time - discr_root))
        high = np.ceil(0.5*(avaliable_time + discr_root))
    
    # count the number of points that are solutions > record_dist
    ways_to_beat = int(high - low)

    #for h in range(int(low), int(high)):
    #    if CalcDist(avaliable_time, h) > record_dist:
    #        ways_to_beat += 1
        
    
    return ways_to_beat

def main():
    start = time.time()
    ### --- Part 1 --- ###
    #sol = 1
    #
    #for race_stats in day5_input:
    #    sol *= IsRecordBeat(race_stats)
    
    ### --- --- ###

    ### --- Part 2 --- ####
    sol = IsRecordBeat(day5_input_p2)
    
    ### --- --- ###

    end = time.time()
    print(sol)
    print(f"Execution time (ms): {(end-start)*10**3}")
##
#
# run  program
if __name__ == '__main__':
    main()

