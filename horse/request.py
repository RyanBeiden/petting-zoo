from models.horse import Horse

def create_horse():
    harriet = Horse("Harriet", "Racing")
    return print(f'| {harriet.name} the {harriet.species} horse is walking on {harriet.date_added} |')
