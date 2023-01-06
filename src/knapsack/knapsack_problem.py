
from knapsack.warehouse import Warehouse
from knapsack.knapsack import Knapsack

class KnapsackProblem():
    def __init__(self):
        self.warehouse = Warehouse()
        self.knapsack = Knapsack(400)

    def __len__(self):
        return len(self.warehouse)

    def evaluate_ga(self, individual):
        self.knapsack.empty()
        self.knapsack.add_items(self.warehouse.filter(individual))
        return self.knapsack.value