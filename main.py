class Backpack:

    max_num_items = 10
    
    def __init__(self, color, tamaño):
        self._items = []
        self.color = color
        self.size = tamaño

    def get_items(self):
        return self._items
    
    def set_items(self, item):
        if isinstance(item, str) and item.isalpha():
            self._items.append(item)
        else:
            print("That's not a real item")

my_bag = Backpack('red', 14)
print(my_bag.get_items())
my_bag.set_items('Scissors')
print(my_bag.get_items())