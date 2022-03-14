class Backpack:

    max_num_items = 10
    
    def __init__(self, color, tamaño):
        self._items = []
        self.color = color
        self.size = tamaño

    def get_items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item, str) and item.isalpha():
            self._items.append(item)
        else:
            print("Please enter a valid item")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0

    def has_item(self, item):
        return item in self._items