import numpy as np

from genetic_algorithm import GeneticAlgorithm


# Objective function
def objective_function(x):
    return x * np.sin(10 * np.pi * x) + 1


# Create Genetic Algorithm
ga = GeneticAlgorithm(
    fitness_function=objective_function,
    bounds=(-1, 2),
    population_size=50,
    generations=100,
    mutation_rate=0.1,
    crossover_rate=0.8,
    maximize=True
)


# Run the algorithm
best_solution, best_fitness, history = ga.run()


# Display results
print("\n========== GENETIC ALGORITHM RESULTS ==========")

print(f"Best Solution (x): {best_solution:.6f}")

print(f"Best Fitness: {best_fitness:.6f}")

print(f"Number of Generations: {len(history)}")

print("===============================================\n")

