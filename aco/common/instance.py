from aco.common import helpers
from aco.common.ant import Ant
import numpy as np
import math


class Instance:

    def __init__(self, coordinates):

        self.coordinates = coordinates
        self.n = len(self.coordinates)
        self.dimension = len(self.coordinates[0])
        self.distances = self._compute_distances()
        self.nn_list = self._compute_nn_list()

    def _compute_distances(self):
        distances = []

        for first in self.coordinates:
            distances.append([])
            for second in self.coordinates:
                distance = helpers.distance(first, second)
                distances[-1].append(distance)

        return distances


    def _compute_nn_list(self):
        nn_list = np.argsort(self.distances, axis=1).tolist()

        for row in nn_list:
            row.append(row.pop(0))

        return nn_list


    def print(self):

        helpers.write_matrix_to_file('distances.txt', self.distances)
        helpers.write_matrix_to_file('nn_list.txt', self.nn_list)

    def calc_tour_len(self, tour: list):

        length = 0

        for i in range(len(tour) - 1):
            length += self.distances[tour[i]][tour[i + 1]]

        return length

    def nn_tour(self):

        ant = Ant()

        while True:

            next_node = None
            distances = self.distances[ant.current_node]
            min_distance = math.inf

            for node in range(self.n):
                if node not in ant.visited:
                    distance = distances[node]
                    if distance < min_distance:
                        next_node = node
                        min_distance = distance

            if next_node is None:
                next_node = ant.tour[0]
                ant.move(next_node)
                break
            else:
                ant.move(next_node)
