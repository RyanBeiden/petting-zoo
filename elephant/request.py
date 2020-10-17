from models.elephant import Elephant

def create_elephant():
    steve = Elephant("Steve", "White", "morning")
    return print(f'| {steve.name} the {steve.species} elephant is available to pet during the {steve.shift} shift. |')
