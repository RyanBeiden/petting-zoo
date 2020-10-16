from models.snake import Snake

def create_snake():
    sawyer = Snake("Sawyer", "Sthnake")
    return print(f'| {sawyer.name} the {sawyer.species} snake is slithering on {sawyer.date_added} |')
