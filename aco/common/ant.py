import math

class Ant:


    def __init__(self, node=0):

        self.tour = []
        self.visited = set()

        self.move(node)

    @property
    def position(self):
        return len(self.tour) - 1

    @property
    def current_node(self):
        return self.tour[self.position]

    def move(self, node):

        self.tour.append(node)
        self.visited.add(node)

    def choose_closest_next(self):

        assert 0 <= self.position < self.n - 1

        current_node = self.tour[self.position]
        min_distance = math.inf

        for node in range(self.n):
            if not self.visited[node]:
                distance = self.instance.distances[current_node][node]
                if distance < min_distance:
                    next_node = node
                    min_distance = distance

        assert next_node

        return next_node

    @property
    def tour_length(self):

        tour_length = 0
        distances = self.instance.distances

        for i in range(self.n):
            distance = distances[self.tour[i]][self.tour[i + 1]]
            tour_length += distance

        return tour_length

    @classmethod
    def nn_tour(cls, instance):

        ant = cls()

        while True:

            next_node = None
            distances = instance.distances[ant.current_node]
            min_distance = math.inf

            for node in range(instance.n):
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
