import numpy as np

class GeneticAlgorithm:
    def __init__(self, func, bounds, pop_size, child_size, mutation_rate, n_iter):
        """
        func: objective function to minimize
        bounds: list of (min, max) for each dimension
        pop_size: number of individuals in parent population
        child_size: number of offspring to generate each generation
        mutation_rate: probability threshold for crossover vs mutation (real-valued)
        n_iter: number of generations to run
        """
        self.func = func
        self.bounds = np.array(bounds)
        self.pop_size = pop_size
        self.child_size = child_size
        self.mutation_rate = mutation_rate
        self.n_iter = n_iter
        self.dim = len(bounds)

    def initialize_population(self):
        lower, upper = self.bounds[:, 0], self.bounds[:, 1]
        pop = np.random.uniform(lower, upper, size=(self.pop_size, self.dim))
        return pop

    def evaluate(self, population):
        # Compute objective values for minimization
        return np.apply_along_axis(self.func, 1, population)

    def select_survivors(self, parents, offspring):
        # Combine and select best individuals (elitism)
        combined = np.vstack((parents, offspring))
        fitness = self.evaluate(combined)
        idx = np.argsort(fitness)  # ascending: lower objective is better
        survivors = combined[idx[:self.pop_size]]
        best_idx = idx[0]
        return survivors, combined[best_idx], fitness[best_idx]

    def crossover(self, parent1, parent2):
        # Real-valued uniform arithmetic crossover
        alpha = np.random.rand(self.dim)
        child = alpha * parent1 + (1 - alpha) * parent2
        return child

    def mutate(self, individual):
        # Random resetting mutation with probability (1 - mutation_rate)
        if np.random.rand() > self.mutation_rate:
            # full random reset within bounds
            lower, upper = self.bounds[:, 0], self.bounds[:, 1]
            individual = np.random.uniform(lower, upper, size=self.dim)
        return individual

    def run(self):
        # Histories
        best_fitness = np.zeros(self.n_iter)
        best_individuals = np.zeros((self.n_iter, self.dim))
        pop_history = []

        # Initialize
        population = self.initialize_population()
        initial_fit = self.evaluate(population)
        best_idx = np.argmin(initial_fit)
        best_fitness[0] = initial_fit[best_idx]
        best_individuals[0] = population[best_idx]
        pop_history.append(population.copy())

        # Generations
        for t in range(1, self.n_iter):
            offspring = np.zeros((self.child_size, self.dim))
            for i in range(self.child_size):
                if np.random.rand() < self.mutation_rate:
                    # Crossover
                    p1, p2 = population[np.random.randint(0, self.pop_size)], \
                             population[np.random.randint(0, self.pop_size)]
                    child = self.crossover(p1, p2)
                else:
                    # Mutation by random resetting
                    idx = np.random.randint(0, self.pop_size)
                    child = self.mutate(population[idx].copy())
                offspring[i] = child

            # Selection with elitism
            population, best_ind, best_fit = self.select_survivors(population, offspring)
            best_fitness[t] = best_fit
            best_individuals[t] = best_ind
            pop_history.append(population.copy())

        return {
            'best_fitness': best_fitness,
            'best_individuals': best_individuals,
            'pop_history': pop_history
        }
