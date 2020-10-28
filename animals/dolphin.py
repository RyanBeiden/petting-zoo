from .animal import Animal
from movements import Walking, Swimming

class Dolphin(Animal, Walking, Swimming):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        self.shift = shift
    
    def blow(self): 
        print("The dolphin blows. A lot")

    def run(self):
        print(f'{self} paddles')

    def __str__(self):
        return f'{self.name} the Dolphin'