import math

def distance(first, second):

    xd = first[0] - second[0]
    yd = first[1] - second[1]

    distance = int(math.sqrt(xd * xd + yd * yd) + 0.5)

    return distance


def write_matrix_to_file(file_path, matrix):

    with open(file_path, 'w') as f:
        for row in matrix:
            f.write(' '.join([str(item) for item in row]))
            f.write('\n')
