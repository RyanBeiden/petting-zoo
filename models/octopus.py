from datetime import date
from animals import Animal

class Octopus(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} while holding the food with all 8 tentacles on {date.today().strftime("%m/%d/%Y")}')
