from aco.common import helpers
import numpy as np


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
