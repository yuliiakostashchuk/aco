import math
import random

class Ant:


    def __init__(self, instance):

        self.instance = instance
        self.n = self.instance.n
        self.tour = [None for i in range(self.n + 1)]
        self.visited = [False for i in range(self.n)]

    def empty_memory(self):

        for visited in self.visited:
            visited = False

    def place(self, step, node):

        self.tour[step] = node
        self.visited[node] = True

    def choose_closest_next(self, step):

        next_city = self.n
        assert 0 < step < self.n

        current_city = self.tour[step - 1]
        min_distance = math.inf

        for city in range(self.n):
            if not self.visited[city]:
                distance = self.instance.distances[current_city][city]
                if distance < min_distance:
                    next_city = city
                    min_distance = distance

        assert 0 <= next_city < self.n

        return next_city

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