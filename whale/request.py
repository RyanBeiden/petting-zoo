from models.whale import Whale

def create_whale():
    bob = Whale("Bob", "Sea")
    return print(f'| {bob.name} the {bob.species} whale is swimming on {bob.date_added} |')
