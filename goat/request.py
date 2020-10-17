from models.goat import Goat

def create_goat():
    lawrence = Goat("Lawrence", "Fainting", "midday")
    return print(f'| {lawrence.name} the {lawrence.species} goat is available to pet during the {lawrence.shift} shift. |')
