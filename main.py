class Backpack:
    
    def __init__(self, color, tamaño):
        self.items = []
        self.color = color
        self.size = tamaño

my_bag = Backpack('red', 14)
my_bag.items.append('pencil')
print(my_bag.items)