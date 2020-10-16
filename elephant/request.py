from models.elephant import Elephant

def create_elephant():
    steve = Elephant("Steve", "White")
    return print(f'| {steve.name} the {steve.species} elephant is walking on {steve.date_added} |')
