def create_attractions_with_animals():
    # Imported when this function is called to prevent a circular dependency
    from animals import Llama, Lion, Horse, Goat, Elephant, Dolphin, Octopus, Seahorse, Shark, Whale, Lizard, Snail, Snake, Spider, Worm, PettingZoo, SnakePit, Wetlands

    varmint_village = PettingZoo("Varmint Village", "A place for cuddles")
    wet_place = Wetlands("Wet Place", "Wet & Gross")
    snake_sack = SnakePit("Snake Sack", "Slimy & Weird")


    tina = Llama("Tina", "fat lard", "morning", "Llama Chow", 874191)
    aslan = Lion("Aslan", "huge", "afternoon", "meat", 874191)
    harriet = Horse("Harriet", "racing", "afternoon", "grass", 874191)
    lawrence = Goat("Lawrence", "fainting", "midday", "straw", 874191)
    steve = Elephant("Steve", "white", "morning", "trees", 874191)
    varmint_village.add_animals(tina)
    varmint_village.add_animals(aslan)
    varmint_village.add_animals(harriet)
    varmint_village.add_animals(lawrence)
    varmint_village.add_animals(steve)


    joe = Dolphin("Joe", "baiji", "morning", "fishies", 874191)
    larry = Octopus("Larry", "cyanea", "morning", "ink", 874191)
    gary = Seahorse("Gary", "baiji", "morning", "plankton", 874191)
    jerry = Shark("Jerry", "great white", "afternoon", "human leg", 874191)
    bob = Whale("Bob", "sea", "midday", "bubbles", 874191)
    wet_place.add_animals(joe)
    wet_place.add_animals(larry)
    wet_place.add_animals(gary)
    wet_place.add_animals(jerry)
    wet_place.add_animals(bob)


    gilbert = Lizard("Gilbert", "shiny", "midday", "ants", 874191)
    sam = Snail("Sam", "slow", "afternoon", "slime", 874191)
    sawyer = Snake("Sawyer", "sthnake", "afternoon", "rat", 874191)
    satan = Spider("Satan", "scary & gross", "afternoon", "nothing", 874191)
    wilbur = Worm("Wilbur", "sticky", "morning", "little worms", 874191)
    snake_sack.add_animals(gilbert)
    snake_sack.add_animals(sam)
    snake_sack.add_animals(sawyer)
    snake_sack.add_animals(satan)
    snake_sack.add_animals(wilbur)

    return varmint_village, wet_place, snake_sack


def main():
    attractions_with_animals = create_attractions_with_animals()
    
    for attraction in attractions_with_animals:
        print(f'{attraction.attraction_name}, {attraction.description}')
        for animal in attraction.animals:
            print(f'* {animal.name} the {animal.species}')
