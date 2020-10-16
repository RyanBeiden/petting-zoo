from models.dolphin import Dolphin

def create_dolphin():
    joe = Dolphin("Joe", "Baiji")
    return print(f'| {joe.name} the {joe.species} dolphin is swimming on {joe.date_added} |')
