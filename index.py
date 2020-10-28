from animals import Dolphin
from attractions import Wetlands

def main():
    joe = Dolphin("Joe", "baiji", "morning", "fishies", 874191)

    a_wet_place = Wetlands("A Wet Place", "real, real wet that's for sure.")
    a_wet_place.add_animal(joe)

    for animal in a_wet_place.animals:
        print(animal)
