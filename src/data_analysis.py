from matplotlib import pyplot as plt
from seaborn import set_style
from ga.genetic_algorithm import GeneticAlgorithm
from one_max.one_max_problem import OneMaxProblem
from knapsack.knapsack_problem import KnapsackProblem
from random import seed

def fine_tuning(evaluation_function, individual_lengths = [], population_sizes = [], generation_tresholds = [], crossover_probabilities = [], mutation_probabilities = [], hall_of_fame_sizes = [], dir="."):
    
    for individual_length in individual_lengths:
        for population_size in population_sizes:
            for generation_threshold in generation_tresholds:
                for crossover_probability in crossover_probabilities:
                    for mutation_probability in mutation_probabilities:
                        for hall_of_fame_size in hall_of_fame_sizes:
                            set_style("whitegrid")
                            plt.xlabel("Generations")
                            plt.ylabel("Fitness over generations")
                            _, max_fitnesses, avg_fitnesses, _ = GeneticAlgorithm(individual_length, hall_of_fame_size, evaluation_function).run(population_size, crossover_probability, mutation_probability, generation_threshold)
                            
                            plt.plot(max_fitnesses, color="red")
                            max_fitness = max(max_fitnesses)
                            x = max_fitnesses.index(max_fitness)
                            plt.plot(avg_fitnesses, color="green")
                            plt.legend(["Max fitness", "Average fitness"])
                            plt.annotate(f"{x,max_fitness}", (x, max_fitness), xycoords='data', xytext=(1, 1.1), textcoords='axes fraction', arrowprops=dict(facecolor='black', shrink=0.05), horizontalalignment='right', verticalalignment='top')
                            plt.savefig(f"{dir}/figure_{individual_length}_{population_size}_{generation_threshold}_{crossover_probability}_{mutation_probability}_{hall_of_fame_size}.png")
                            plt.clf()

probabilities = [ i / 10 for i in range(1,11)]
sizes = [ i for i in range(100, 1000, 100) ]
thresholds = [ i for i in range(10, 110, 10)]

# We set the seed to obtain same pseudo-random number sequence
seed(42)

omp = OneMaxProblem()

# Analyze populations sizes
fine_tuning(omp.evaluate_ga,[100], sizes, [50], [0.9], [0.1], [10], "figures/omp/population")

# Analyze individual sizes
fine_tuning(omp.evaluate_ga, sizes, [200], [50], [0.9], [0.1], [10], "figures/omp/individual_length")

# Analyze crossover probabilities
fine_tuning(omp.evaluate_ga, [100], [200], [50], probabilities, [0.1], [10], "figures/omp/crossover")

# Analyze mutation probabilities
fine_tuning(omp.evaluate_ga, [100], [200], [50], [0.9], probabilities, [10], "figures/omp/mutation")

knapsack_problem = KnapsackProblem()
fine_tuning(knapsack_problem.evaluate_ga, [len(knapsack_problem)], [50],[50], [0.9], [0.1], [1], "figures/knapsack")