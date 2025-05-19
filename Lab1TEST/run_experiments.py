import os
import pickle

from fitness import FUNCTIONS
from genetic import GeneticAlgorithm

# Number of generations for all experiments
N_ITER = 100

# Define hyperparameter sets
param_sets = [
    {"pop_size": 50,  "child_size": 40,  "mutation_rate": 0.5},
    {"pop_size": 50,  "child_size": 100, "mutation_rate": 1.0},
    {"pop_size": 100, "child_size": 40,  "mutation_rate": 0.5},
    {"pop_size": 100, "child_size": 100, "mutation_rate": 1.0},
]

# Directory to store results
RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'results')


def main():
    # Create results directory if it does not exist
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Iterate over all fitness functions and parameter sets
    for func_name, info in FUNCTIONS.items():
        func = info['func']
        bounds = info['bounds']
        for params in param_sets:
            pop_size = params['pop_size']
            child_size = params['child_size']
            mutation_rate = params['mutation_rate']

            print(f"Running GA for {func_name} with pop_size={pop_size}, child_size={child_size}, mutation_rate={mutation_rate}")
            ga = GeneticAlgorithm(
                func=func,
                bounds=bounds,
                pop_size=pop_size,
                child_size=child_size,
                mutation_rate=mutation_rate,
                n_iter=N_ITER
            )
            results = ga.run()

            # Save results to file
            filename = f"{func_name}_pop{pop_size}_child{child_size}_mut{mutation_rate}.pkl"
            filepath = os.path.join(RESULTS_DIR, filename)
            with open(filepath, 'wb') as f:
                pickle.dump(results, f)

            print(f"Saved results to {filepath}")

    print("All experiments completed.")


if __name__ == '__main__':
    main()
