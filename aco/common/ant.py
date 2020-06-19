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
