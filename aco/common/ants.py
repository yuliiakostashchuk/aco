import random
from aco.common.ant import Ant

def nn_tour(instance):

    ant = Ant(instance)

    step = 0

    node = random.randint(0, instance.n - 1)

    ant.place(step, node)

    while step < instance.n - 1:
        step += 1
        next_city = ant.choose_closest_next(step)
        ant.place(step, next_city)

    ant.tour[instance.n] = ant.tour[0]

    return ant.tour_length
