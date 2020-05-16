import math
from math import pi

def get_circumference(radius, n):
    points = []
    for i in range(n):
        points.append((int(radius*math.cos(2*pi/n*i)), int(radius*math.sin(2*pi/n*i))))
    return points

if __name__ == '__main__':
    pass
