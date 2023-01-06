from numpy import array
from knapsack.item import Item

default_items = [
    Item("map", 9, 150),
    Item("compass", 13, 35),
    Item("water", 153, 200),
    Item("sandwich", 50, 160),
    Item("glucose", 15, 60),
    Item("tin", 68, 45),
    Item("banana", 27, 60),
    Item("apple", 39, 40),
    Item("cheese", 23, 30),
    Item("beer", 52, 10),
    Item("suntan cream", 11, 70),
    Item("camera", 32, 30),
    Item("t-shirt", 24, 15),
    Item("trousers", 48, 10),
    Item("umbrella", 73, 40),
    Item("waterproof trousers", 42, 70),
    Item("waterproof overclothes", 43, 75),
    Item("note-case", 22, 80),
    Item("sunglasses", 7, 20),
    Item("towel", 18, 12),
    Item("socks", 4, 50),
    Item("book", 30, 10)
]
class Warehouse:

    def __init__(self, items = default_items):
        self.items = array(items)

    def __len__(self):
        return len(self.items)
    
    def filter(self, selected_items):
       selected_items = list(map(lambda x: x == 1, selected_items))
       return self.items[selected_items]
        