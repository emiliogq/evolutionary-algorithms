from random import seed
from genetic_algorithm import GeneticAlgorithm

def test_one_max_problem():
    seed(42)
    best_individual, _, _ = GeneticAlgorithm(100).run(200, 0.9, 0.1, 50)
    expected = [1]*100
    assert best_individual == expected