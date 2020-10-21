from animals.animals import create_attractions_with_animals

def main():
    attractions_with_animals = create_attractions_with_animals()
    
    for attraction in attractions_with_animals:
        print(f'{attraction.attraction_name}, {attraction.description}')
        for animal in attraction.animals:
            print(f'* {animal.name} the {animal.species}')
