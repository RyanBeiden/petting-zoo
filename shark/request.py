from models.shark import Shark

def create_shark():
    jerry = Shark("Jerry", "Great White")
    return print(f'| {jerry.name} the {jerry.species} shark is swimming on {jerry.date_added} |')
