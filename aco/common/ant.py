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

    def place(self, step):

        rnd = random.randint(0, self.n - 1)

        self.tour[step] = rnd
        self.visited[rnd] = True