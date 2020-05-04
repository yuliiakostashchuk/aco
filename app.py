import datetime

def main():
    start_time = datetime.datetime.now()
    with open('eil51.tsp') as f:
        for line in f:
            if line.startswith('DIMENSION :'):
                print(line.split()[-1])
            if line.startswith('NODE_COORD_SECTION'):
                print('found section containing the node coordinates')
                break
    elapsed = datetime.datetime.now() - start_time
    print(elapsed.seconds, elapsed.microseconds)

if __name__ == '__main__':
    main()
