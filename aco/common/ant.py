

class Ant:


    def __init__(self, instance):

        self.instance = instance
        self.n = self.instance.n
        self.tour = [None for i in range(self.n + 1)]
        self.visited = [False for i in range(self.n)]