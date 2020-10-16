from models.seahorse import Seahorse

def create_seahorse():
    gary = Seahorse("Gary", "Baiji")
    return print(f'| {gary.name} the {gary.species} seahorse is swimming on {gary.date_added} |')
