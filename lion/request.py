from models.lion import Lion

def create_lion():
    aslan = Lion("Aslan", "Huge", "afternoon")
    return print(f'| {aslan.name} the {aslan.species} lion is available to pet during the {aslan.shift} shift. |')
