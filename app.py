import argparse
import datetime

def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--tries", type=int)
    parser.add_argument("--tours", type=int)
    # parser.add_argument("--seed") # TODO
    parser.add_argument("--time", type=float)
    # parser.add_argument("--tsplibfile") # TODO
    parser.add_argument("--optimum", type=int)
    parser.add_argument("--ants", type=int)
    parser.add_argument("--nnants", type=int)
    parser.add_argument("--alpha", type=float)
    parser.add_argument("--beta", type=float)
    parser.add_argument("--rho", type=float)
    parser.add_argument("--q0", type=float)
    parser.add_argument("--elitistants", type=int)
    parser.add_argument("--rasranks", type=int)
    parser.add_argument("--nnls", type=int)
    parser.add_argument("--localsearch", type=int)
    # parser.add_argument("--dlb") # TODO
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--asys", action='store_true')
    group.add_argument("--eas", action='store_true')
    # group.add_argument("--ras", action='store_true')
    group.add_argument("--mmas", action='store_true')
    # group.add_argument("--bwas", action='store_true')
    group.add_argument("--acs", action='store_true')
    parser.add_argument("--quiet", action='store_true')

    return parser

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

def set_default_as_parameters():
    parameters = {
        "n_ants": -1,
        "nn_ants": 20,
        "alpha": 1.0,
        "beta": 2.0,
        "rho": 0.5,
        "q_0": 0.0,
        "ras_ranks": 0,
        "elitist_ants": 0
    }
    return parameters

def set_default_eas_parameters():
    parameters = {
        "n_ants": -1,
        "nn_ants": 20,
        "alpha": 1.0,
        "beta": 2.0,
        "rho": 0.5,
        "q_0": 0.0,
        "ras_ranks": 0,
        "elitist_ants": -1
    }
    return parameters

def set_default_mmas_parameters():
    parameters = {
        "n_ants": -1,
        "nn_ants": 20,
        "alpha": 1.0,
        "beta": 2.0,
        "rho": 0.02,
        "q_0": 0.0,
        "ras_ranks": 0,
        "elitist_ants": 0
    }
    return parameters

def set_default_acs_parameters():
    parameters = {
        "n_ants": 10,
        "nn_ants": 20,
        "alpha": 1.0,
        "beta": 2.0,
        "rho": 0.1,
        "q_0": 0.9,
        "ras_ranks": 0,
        "elitist_ants": 0
    }
    return parameters

def set_default_ls_parameters(parameters):
    ls_parameters = {
        "dlb_flag": True,
        "nn_ls": 20,
        "n_ants": 25,
        "nn_ants": 20,
        "alpha": 1.0,
        "beta": 2.0,
        "rho": 0.5,
        "q_0": 0.0,
    }
    if parameters["mmas_flag"]:
        ls_parameters["n_ants"] = 25
        ls_parameters["rho"] = 0.2
        ls_parameters["q_0"] = 0.00
    if parameters["acs_flag"]:
        ls_parameters["n_ants"] = 10
        ls_parameters["rho"] = 0.1
        ls_parameters["q_0"] = 0.98
    if parameters["eas_flag"]:
        ls_parameters["elitist_ants"] = 25
    return ls_parameters

def main():
    start_time = datetime.datetime.now()
    parser = create_parser()
    args = parser.parse_args()
    parameters = set_default_parameters()
    if args.time is not None:
        parameters["max_time"] = args.time
    if args.tries is not None:
        parameters["max_tries"] = args.tries
    if args.tours is not None:
        parameters["max_tours"] = args.tours
    if args.optimum is not None:
        parameters["optimal"] = args.optimum
    parameters["as_flag"] = args.asys
    parameters["eas_flag"] = args.eas
    # parameters["ras_flag"] = args.ras
    parameters["mmas_flag"] = args.mmas
    # parameters["bwas_flag"] = args.bwas
    parameters["acs_flag"] = args.acs

    if parameters["as_flag"]:
        parameters.update(set_default_as_parameters())
    if parameters["eas_flag"]:
        parameters.update(set_default_eas_parameters())
    if parameters["mmas_flag"]:
        parameters.update(set_default_mmas_parameters())
    if parameters["acs_flag"]:
        parameters.update(set_default_acs_parameters())

    if args.localsearch is not None:
        parameters["ls_flag"] = args.localsearch

    if parameters["ls_flag"]:
        parameters.update(set_default_ls_parameters(parameters))

    if args.ants is not None:
        parameters["n_ants"] = args.ants
    if args.nnants is not None:
        parameters["nn_ants"] = args.nnants
    if args.alpha is not None:
        parameters["alpha"] = args.alpha
    if args.beta is not None:
        parameters["beta"] = args.beta
    if args.rho is not None:
        parameters["rho"] = args.rho
    if args.q0 is not None:
        parameters["q_0"] = args.q0
    if args.elitistants is not None:
        parameters["elitist_ants"] = args.elitistants
    if args.rasranks is not None:
        parameters["ras_ranks"] = args.rasranks
    if args.nnls is not None:
        parameters["nn_ls"] = args.nnls
    # if args.dlb is not None:
    #     parameters["dlb_flag"] = args.dlb

    print('Parameters:\n', parameters)

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
