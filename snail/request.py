from models.snail import Snail

def create_snail():
    sam = Snail("Sam", "Slow")
    return print(f'| {sam.name} the {sam.species} snail is slithering on {sam.date_added} |')
