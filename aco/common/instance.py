from aco.common import helpers


class Instance:

    def __init__(self, coordinates):

        self.coordinates = coordinates
        self.n = len(self.coordinates)
        self.dimension = len(self.coordinates[0])
        self.distances = self._compute_distances()

    def _compute_distances(self):
        distances = []

        for first in self.coordinates:
            distances.append([])
            for second in self.coordinates:
                distance = helpers.distance(first, second)
                distances[-1].append(distance)

        return distances
