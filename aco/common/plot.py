import math
from math import pi
import plotly.graph_objects as go

def get_circumference(radius, n):
    points = []
    for i in range(n):
        points.append((int(radius*math.cos(2*pi/n*i)), int(radius*math.sin(2*pi/n*i))))
    return points

def get_sphere(radius, n):
    points = []
    for i in range(n):
        theta = 2*pi/n*i
        for j in range(n):
            phi = 2*pi/n*j
            x = int(radius * math.sin(theta) * math.cos(phi))
            y = int(radius * math.sin(theta) * math.sin(phi))
            z = int(radius * math.cos(theta))
            points.append((x, y, z))

    return points

def get_grid(n, a):
    points = []
    for i in range(0, n * a, a):
        for j in range(0, n * a, a):
            points.append((i, j))
    return points

def get_cube(n, a):
    points = []
    for i in range(0, n * a, a):
        for j in range(0, n * a, a):
            for k in [0, (n - 1) * a]:
                points.append((i, j, k))
                points.append((k, i, j))
                points.append((i, k, j))
    return list(set(points))

def extract_coordinates(points):

    coordinates = []

    for i in range(len(points[0])):
        coordinates.append([point[i] for point in points])

    return coordinates

if __name__ == '__main__':

    radius = 100
    n = 20
    a = 2
    m = 3

    # Get coordinates

    circumference_points = get_circumference(radius, n)
    sphere_points = get_sphere(radius, n)
    grid_points = get_grid(n, a)
    cube_points = get_cube(m, a)

    circumference_coordinates = extract_coordinates(circumference_points)
    sphere_coordinates = extract_coordinates(sphere_points)
    grid_coordinates = extract_coordinates(grid_points)
    cube_coordinates = extract_coordinates(cube_points)

    # Plot figures

    circumference = go.Figure(data=go.Scatter(x=circumference_coordinates[0], y=circumference_coordinates[1], mode='markers'))
    circumference.update_layout(width=1000, height=1000)

    sphere = go.Figure(data=go.Scatter3d(x=sphere_coordinates[0], y=sphere_coordinates[1], z=sphere_coordinates[2], mode='markers'))

    grid = go.Figure(data=go.Scatter(x=grid_coordinates[0], y=grid_coordinates[1], mode='markers'))
    grid.update_layout(width=1000, height=1000)

    cube = go.Figure(data=go.Scatter3d(x=cube_coordinates[0], y=cube_coordinates[1], z=cube_coordinates[2], mode='markers'))

    circumference.show()
    sphere.show()
    grid.show()
    cube.show()
