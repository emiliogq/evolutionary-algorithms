from deap.base import Toolbox, Fitness
from deap.tools import initRepeat, selTournament, cxOnePoint, mutFlipBit, Statistics
from deap.algorithms import eaSimple
from deap import creator

from numpy import max, mean
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
    
        self.stats = Statistics(lambda individual: individual.fitness.values)
        self.stats.register("max", max)
        self.stats.register("avg", mean)

    def run(self, population_size, crossover_probability, mutation_probability, generation_threshold):
        
        population = self.toolbox.create_population(n=population_size)
        population, logbook = eaSimple(population, self.toolbox, crossover_probability, mutation_probability, generation_threshold, self.stats, verbose=True)
        generations, max_fitnesses, avg_fitnesses = logbook.select("gen", "max", "avg")
        
        fitnesses = [individual.fitness.values[0] for individual in population]
        max_fitness = max(fitnesses)
        best_individual = population[ fitnesses.index(max_fitness) ]

        return best_individual, max_fitnesses, avg_fitnesses
