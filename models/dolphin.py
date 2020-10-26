from datetime import date

class Dolphin():

    def __init__(self, name, species, shift, food, chip_number):
        self.name = name
        self.species = species
        self.shift = shift
        self.swimming = True
        self.date_added = date.today()
        self.food = food
        self.__chip_number = chip_number

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
    
    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, number):
        pass
