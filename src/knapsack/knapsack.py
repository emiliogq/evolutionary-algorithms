
from knapsack.item import Item

class Knapsack:
    def __init__(self, max_capacity = 0, items = []):
        self.items = items
        self.weight = 0
        self.value = 0
        self.max_capacity = max_capacity
        self.str = ""

    def empty(self):
        self.items.clear()
        self.weight, self.value = 0, 0

    def add_item(self, item: Item):
        is_addable = self.weight + item.weight < self.max_capacity
        if is_addable :
            self.items.append(item)
            self.weight += item.weight
            self.value +=  item.value
            self.str += f"- Adding {item.name}: weight = {item.weight}, value = {item.value}, accumulated weight = {self.weight}, accumulated value = {self.value} \n"

    def add_items(self, items):
        for item in items: 
            self.add_item(item)
    
    def __str__(self):
        return self.str

                
    # def add_item(self, name:str, weight, value):
    #     self.items.append(KnapsackItem(name, weight, value))