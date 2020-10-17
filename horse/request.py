from models.horse import Horse

def create_horse():
    harriet = Horse("Harriet", "Racing", "morning")
    return print(f'| {harriet.name} the {harriet.species} horse is available to pet during the {harriet.shift} shift. |')
