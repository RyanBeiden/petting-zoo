from models.goat import Goat

def create_goat():
    lawrence = Goat("Lawrence", "Fainting")
    return print(f'| {lawrence.name} the {lawrence.species} goat is walking on {lawrence.date_added} |')
