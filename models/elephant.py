from datetime import date
from animals import Animal

class Elephant(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} to help his big big stomach on {date.today().strftime("%m/%d/%Y")}')
