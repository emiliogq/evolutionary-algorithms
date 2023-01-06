from numpy.random import randint, seed
from one_max.one_max_problem import OneMaxProblem
seed(42)

def test_one_max_problem():
    individual_length = 100
    randomized_binary_permutation = randint(2, size=individual_length)
    omp = OneMaxProblem()
    expected = 56
    assert omp.evaluate_ga(randomized_binary_permutation) == expected