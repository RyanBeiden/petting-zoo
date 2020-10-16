from models.lion import Lion

def create_lion():
    aslan = Lion("Aslan", "Huge")
    return print(f'| {aslan.name} the {aslan.species} lion is walking on {aslan.date_added} |')
