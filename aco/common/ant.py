import math
import random

class Ant:


    def __init__(self, instance, node):

        self.instance = instance
        self.n = self.instance.n
        self.tour = [None for i in range(self.n + 1)]
        self.visited = [False for i in range(self.n)]
        self.position = None

        self.position = 0
        self.tour[self.position] = node
        self.visited[node] = True

    def move(self, node):

        assert 0 <= self.position < self.n - 1

        self.position += 1

        self.tour[self.position] = node
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


    def nn_tour(self):

        step = 0

        node = random.randint(0, self.n - 1)

        self.place(step, node)