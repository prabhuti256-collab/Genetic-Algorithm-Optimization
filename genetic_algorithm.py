import numpy as np


class GeneticAlgorithm:

    def __init__(
        self,
        fitness_function,
        bounds=(-10, 10),
        population_size=50,
        generations=100,
        mutation_rate=0.1,
        crossover_rate=0.8,
        maximize=True
    ):

        self.fitness_function = fitness_function

        self.lower_bound = bounds[0]
        self.upper_bound = bounds[1]

        self.population_size = population_size
        self.generations = generations

        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

        self.maximize = maximize

        self.population = None

        self.best_solution = None
        self.best_fitness = None

        self.history = []
        self.population_history = []


    # --------------------------------------------------
    # INITIALIZE POPULATION
    # --------------------------------------------------

    def initialize_population(self):

        self.population = np.random.uniform(
            self.lower_bound,
            self.upper_bound,
            self.population_size
        )


    # --------------------------------------------------
    # CALCULATE FITNESS
    # --------------------------------------------------

    def calculate_fitness(self):

        return np.array([
            self.fitness_function(x)
            for x in self.population
        ])


    # --------------------------------------------------
    # SELECT PARENTS
    # --------------------------------------------------

    def select_parents(self, fitness):

        selected = []

        for _ in range(self.population_size):

            i, j = np.random.randint(
                0,
                self.population_size,
                2
            )

            if self.maximize:

                winner = (
                    i
                    if fitness[i] > fitness[j]
                    else j
                )

            else:

                winner = (
                    i
                    if fitness[i] < fitness[j]
                    else j
                )

            selected.append(
                self.population[winner]
            )

        return np.array(selected)


    # --------------------------------------------------
    # CROSSOVER
    # --------------------------------------------------

    def crossover(self, parent1, parent2):

        if np.random.random() < self.crossover_rate:

            alpha = np.random.random()

            child1 = (
                alpha * parent1
                + (1 - alpha) * parent2
            )

            child2 = (
                alpha * parent2
                + (1 - alpha) * parent1
            )

            return child1, child2

        return parent1, parent2


    # --------------------------------------------------
    # MUTATION
    # --------------------------------------------------

    def mutate(self, individual):

        if np.random.random() < self.mutation_rate:

            mutation = np.random.normal(
                0,
                0.5
            )

            individual += mutation

        return np.clip(
            individual,
            self.lower_bound,
            self.upper_bound
        )


    # --------------------------------------------------
    # RUN GENETIC ALGORITHM
    # --------------------------------------------------

    def run(self):

        self.initialize_population()

        self.history = []
        self.population_history = []

        self.best_solution = None
        self.best_fitness = None

        for generation in range(self.generations):

            # Calculate fitness
            fitness = self.calculate_fitness()

            # Find current best
            if self.maximize:

                best_index = np.argmax(fitness)

            else:

                best_index = np.argmin(fitness)

            current_best_solution = (
                self.population[best_index]
            )

            current_best_fitness = (
                fitness[best_index]
            )

            # Store global best
            if self.best_fitness is None:

                self.best_solution = (
                    current_best_solution
                )

                self.best_fitness = (
                    current_best_fitness
                )

            elif self.maximize:

                if current_best_fitness > self.best_fitness:

                    self.best_solution = (
                        current_best_solution
                    )

                    self.best_fitness = (
                        current_best_fitness
                    )

            else:

                if current_best_fitness < self.best_fitness:

                    self.best_solution = (
                        current_best_solution
                    )

                    self.best_fitness = (
                        current_best_fitness
                    )

            # Save history
            self.history.append(
                self.best_fitness
            )

            self.population_history.append(
                self.population.copy()
            )

            # Selection
            parents = self.select_parents(
                fitness
            )

            new_population = []

            # Crossover + mutation
            for i in range(
                0,
                self.population_size,
                2
            ):

                parent1 = parents[i]

                if i + 1 < self.population_size:

                    parent2 = parents[i + 1]

                else:

                    parent2 = parents[0]

                child1, child2 = self.crossover(
                    parent1,
                    parent2
                )

                child1 = self.mutate(child1)
                child2 = self.mutate(child2)

                new_population.extend(
                    [child1, child2]
                )

            # Next generation
            self.population = np.array(
                new_population[
                    :self.population_size
                ]
            )

        return (
            self.best_solution,
            self.best_fitness,
            self.history
        )
    