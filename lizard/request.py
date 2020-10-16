from models.lizard import Lizard

def create_lizard():
    gilbert = Lizard("Gilbert", "Shiny")
    return print(f'| {gilbert.name} the {gilbert.species} lizard is slithering on {gilbert.date_added} |')
