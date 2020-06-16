import math

class Ant:


    def __init__(self, node):

        self.tour = [node]
        self.visited = {node: True}

    @property
    def position(self):
        return len(self.tour) - 1

    @property
    def current_node(self):
        return self.tour[self.position]

    def move(self, node):

        self.tour.append(node)
        self.visited[node] = True

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

        node = 0
        ant = cls(node)

        while ant.position < instance.n - 1:

            next_node = None
            distances = instance.distances[ant.current_node]
            min_distance = math.inf

            for node in range(instance.n):
                if not ant.visited[node]:
                    distance = distances[node]
                    if distance < min_distance:
                        next_node = node
                        min_distance = distance

            if next_node is not None:
                ant.move(next_node)

        ant.move(ant.tour[0])
