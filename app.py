def main():
    with open('eil51.tsp') as f:
        for line in f:
            if line.startswith('DIMENSION :'):
                print(line.split()[-1])
            if line.startswith('NODE_COORD_SECTION'):
                print('found section containing the node coordinates')
                break

if __name__ == '__main__':
    main()
