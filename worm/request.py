from models.worm import Worm

def create_worm():
    wilbur = Worm("Wilbur", "Sticky")
    return print(f'| {wilbur.name} the {wilbur.species} worm is slithering on {wilbur.date_added} |')
