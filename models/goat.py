from datetime import date

class Goat():

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.walking = True
        self.shift = shift
        self.date_added = date.today()