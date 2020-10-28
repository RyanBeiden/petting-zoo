from animals import Elephant
from animals import Dolphin
from attractions import PettingZoo

def main():
    varmint_village = PettingZoo("The Varmint Village", "critters that love to be pet!")

    # remember, some animals may require more arguments than others; e.g. shift
    dolly = Elephant("Dolly", "miniature llama", "morning", "hay", 1033)
    snappy = Dolphin("Snappy", "American Alligator", "afternoon", "fish", 1044)

    varmint_village.add_animal(dolly)
    varmint_village.add_animal(snappy)
