import random
import math

class Ant:


    def __init__(self, instance):

        self.instance = instance
        self.n = self.instance.n
        self.tour = [None for i in range(self.n + 1)]
        self.visited = [False for i in range(self.n)]

    def empty_memory(self):

        for visited in self.visited:
            visited = False

    def place(self, step):

        rnd = random.randint(0, self.n - 1)

        self.tour[step] = rnd
        self.visited[rnd] = True

    def choose_closest_next(self, phase):

        next_city = self.n
        assert 0 < phase < self.n
        current_city = self.tour[phase - 1]
        min_distance = math.inf

        for city in range(self.n):
            if not self.visited[city]:
                if self.instance.distances[current_city][city] < min_distance:
                    next_city = city
                    min_distance = self.instance.distances[current_city][city]

        assert 0 <= next_city < self.n

        self.tour[phase] = next_city
        self.visited[next_city] = True

    @property
    def tour_length(self):

        tour_length = 0
        distances = self.instance.distances

        for i in range(self.n):
            distance = distances[self.tour[i]][self.tour[i + 1]]
            tour_length += distance

        return tour_length