import math

def distance(first, second):

    xd = first[0] - second[0]
    yd = first[1] - second[1]

    distance = int(math.sqrt(xd * xd + yd * yd) + 0.5)

    return distance
