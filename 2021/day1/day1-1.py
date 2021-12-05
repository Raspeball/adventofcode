with open("day1-input.txt") as m:
    measurements = [float(line.rstrip()) for line in m]

#print(measurements)

test = [1,2,3,4,3,5,3,6]

def IsLarger(list):

    n_is_larger = 0
    current = list[0]

    for i in list:
        if list.index(i) == 0:
            continue
        else:
            if i > current:
                n_is_larger += 1

        current = i

    return n_is_larger

print(IsLarger(measurements))
