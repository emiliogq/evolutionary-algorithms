from knapsack.knapsack import Knapsack
from knapsack.warehouse import Warehouse
from numpy.random import randint, seed

seed(42)
warehouse = Warehouse()


def test_knapsack():
    randomly_selected_items = randint(2, size=len(warehouse))
    knapsack = Knapsack(400)
    knapsack.add_items(warehouse.filter(randomly_selected_items))
    assert knapsack.value == 355

    knapsack.empty()
    knapsack.add_items(warehouse.filter([1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,1]))
    assert knapsack.value == 700


        

