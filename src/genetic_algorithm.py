from deap.base import Toolbox, Fitness
from deap.tools import initRepeat, selTournament, cxOnePoint, mutFlipBit
from deap import creator

from random import randint, random

class GeneticAlgorithm:
    def __init__(self, individual_length) -> None:
        self.toolbox = Toolbox()
        self.individual_length = individual_length
        self.toolbox.register("zeroOrOne", randint, 0,1)
        
        creator.create("FitnessMax", Fitness, weights=(1.0,))
        
        creator.create("Individual", list, fitness=creator.FitnessMax)
        
        self.toolbox.register("create_individual", initRepeat, creator.Individual, self.toolbox.zeroOrOne, individual_length)
        
        self.toolbox.register("create_population", initRepeat, list, self.toolbox.create_individual)
        
        self.toolbox.register("evaluate", lambda individual: (sum(individual),))
        
        self.toolbox.register("select", selTournament, tournsize=3)

        self.toolbox.register("mate", cxOnePoint)

        attribute_flip_probability = 1.0/individual_length
        self.toolbox.register("mutate", mutFlipBit, indpb=attribute_flip_probability)
    
    def calculate_fitness(self, individuals):
        fitnesses = list(map(self.toolbox.evaluate, individuals))
        for individual, fitness in zip(individuals, fitnesses):
            individual.fitness.values = fitness

    def run(self, population_size, crossover_probability, mutation_probability, generation_threshold):
        max_fitnesses, avg_fitnesses = [], []
        population = self.toolbox.create_population(n=population_size)
        self.calculate_fitness(population)
        fitnesses = [individual.fitness.values[0] for individual in population]
        best_individual = population[0]
        generations = 0
        while max(fitnesses) < self.individual_length and generations < generation_threshold:
            # numpy array
            offspring = self.toolbox.select(population, len(population))

            offspring = list(map(self.toolbox.clone, offspring))
            for first, second in zip(offspring[::2], offspring[1::2]):
                if random() < crossover_probability:
                    self.toolbox.mate(first, second)
                    del first.fitness.values
                    del second.fitness.values

            for mutant in offspring:
                if random() < mutation_probability:
                    self.toolbox.mutate(mutant)
                    del mutant.fitness.values

            fresh_individuals = list(filter(lambda individual : not individual.fitness.valid, offspring))
            self.calculate_fitness(fresh_individuals)
            population[:] = offspring
            fitnesses = [individual.fitness.values[0] for individual in population]

            max_fitness = max(fitnesses)
            
            avg_fitnesses.append(sum(fitnesses) / len(population))
            max_fitnesses.append(max_fitness)

            best_individual = population[ fitnesses.index(max_fitness) ]

            generations += 1

        return best_individual, max_fitnesses, avg_fitnesses
