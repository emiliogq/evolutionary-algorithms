from matplotlib import pyplot as plt
from genetic_algorithm import GeneticAlgorithm

best_individual, max_fitnesses, avg_fitnesses = GeneticAlgorithm(100, 10).run(200, 0.9, 0.1, 50)

plt.plot(max_fitnesses, color="red")
plt.plot(avg_fitnesses, color="green")
plt.xlabel("Generations")
plt.ylabel("Fitness over iterations")
plt.legend(["Max fitness", "Average fitness"])
plt.show()