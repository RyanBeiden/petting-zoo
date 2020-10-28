from . import Animal
from movements import Walking

class Elephant(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
    
    def blow(self): 
        print("The elephant trunks. A lot")

    def run(self):
        print(f'{self} wobbles')

    def __str__(self):
        return f'{self.name} the Elephant'
