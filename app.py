import argparse
import datetime

def create_parser():
    parser = argparse.ArgumentParser()

def set_default_parameters():
    parameters = {
        "ls_flag": 3,
        "dlb_flag": True,
        "nn_ls": 20,
        "n_ants": 25,
        "nn_ants": 20,
        "alpha": 1.0,
        "beta": 2.0,
        "rho": 0.5,
        "q_0": 0.0,
        "max_tries": 10,
        "max_tours": 0,
        "seed": None, # TODO
        "max_time": 10.0,
        "optimal": 1,
        "branch_fac": 1.00001,
        "u_gb": None, # TODO
        "as_flag": False,
        "eas_flag": False,
        # "ras_flag": False,
        "mmas_flag": False,
        # "bwas_flag": False,
        "acs_flag": False,
        "ras_ranks": 0,
        "elitist_ants": 0
    }
    return parameters

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
