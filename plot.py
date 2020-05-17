import math
from math import pi
import plotly.graph_objects as go

def get_circumference(radius, n):
    points = []
    for i in range(n):
        points.append((int(radius*math.cos(2*pi/n*i)), int(radius*math.sin(2*pi/n*i))))
    return points

def extract_coordinates(points):

    coordinates = []

    for i in range(len(points[0])):
        coordinates.append([point[i] for point in points])

    return coordinates

if __name__ == '__main__':

    radius = 100
    n = 20

    points = get_circumference(radius, n)

    coordinates = extract_coordinates(points)

    figure = go.Figure(data=go.Scatter(x=coordinates[0], y=coordinates[1], mode='markers'))
    figure.update_layout(width=1000, height=1000)

    figure.show()
