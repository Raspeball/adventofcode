#
# read file
# day2-input.txt
with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2022\day2\day2-input.txt") as sguide:
    rounds = [(line.strip("\n")).replace(" ", "") for line in sguide]
    rounds[:] = [list(r) for r in rounds]

## Part one ##
def RPS_Result_Score(res):
    # res is a list with two str elements
    # res[0] is either A, B or C (rock, paper, scissors)
    # res[1] is either X, Y or Z (rock, paper, scissors)
    opponent = "ABC"
    strat = "XYZ"
    #
    shape_score = strat.index(res[1]) + 1
    #
    outcome_score = 0
    #
    if opponent.index(res[0]) == strat.index(res[1]):
        outcome_score = 3
    
    else:
        if res[0] == "A":
            if res[1] == "Y":
                outcome_score = 6
            else:
                outcome_score == 0
        
        elif res[0] == "B":
            if res[1] == "X":
                outcome_score = 0
            else:
                outcome_score = 6
        
        else:
            if res[1] == "X":
                outcome_score = 6
            else:
                outcome_score = 0
    
    tot_score = outcome_score + shape_score

    return tot_score

## ##

## Part two ##
def RPS_Result_Score_mod(res):
    # res is a list with two str elements
    # res[0] is either A, B or C (rock, paper, scissors)
    # res[1] is either X, Y or Z (rock, paper, scissors)
    opponent = "ABC"
    strat = "XYZ"
    #
    outcome_score = 0
    #
    if res[1] == "X": # i need to loose
        pass


    return tot_score
#
#
#
def main():

    tot = 0

    for rps in rounds:
        tot += RPS_Result_Score(rps)
    
    print(tot)
#
#
#
# run program #
if __name__ == '__main__':
    main()