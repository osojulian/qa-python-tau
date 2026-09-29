# Parent class 1

class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print(f'the sku is {self.sku}')

#Parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print(f'the section is {self.section} and the type is {self.type}')

#Child class

class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print(f'{self.name} {self.color} on sale!')


Blouse = Shirts('00001', 43, 'Tops', 'Formal Blouse', 'White')

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()



