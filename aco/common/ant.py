
class Ant:

    def __init__(self, node=0):

        self.tour = []
        self.visited = set()

        self.move(node)

    @property
    def node(self):
        return self.tour[-1]

    def move(self, node):

        self.tour.append(node)
        self.visited.add(node)
