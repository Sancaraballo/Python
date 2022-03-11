from curses.ascii import isalpha


class Backpack:

    max_num_items = 10
    
    def __init__(self, color, tamaño):
        self._items = []
        self.color = color
        self.size = tamaño

    def get_items(self):
        return self._items
    
    def set_items(self, item):
        if isinstance(item, str) and isalpha(item):
            self._items.append(item)
        else:
            print("That's not a real item")

my_bag = Backpack('red', 14)
my_bag.items.append('pencil')
print(my_bag.items)