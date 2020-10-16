from models.octopus import Octopus

def create_octopus():
    larry = Octopus("Larry", "Cyanea")
    return print(f'| {larry.name} the {larry.species} octopus is swimming on {larry.date_added} |')
