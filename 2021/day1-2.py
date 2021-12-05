with open("day1-input.txt") as m:
    measurements = [float(line.rstrip()) for line in m]

test = measurements[0:10]

def IsLargerThree(list):

    n_is_larger = 0
    current_threesum = sum(list[0:3])

    for i, val in enumerate(list):
        #print(current_threesum)
        if (i+3) > len(list):
            break
        else:
            next_threesum = sum(list[i:(i+3)])
            #print(next_threesum)

            if  next_threesum > current_threesum:
                n_is_larger += 1

            current_threesum = next_threesum


    return n_is_larger


#print(IsLargerThree(measurements))


print(IsLargerThree(measurements))
