from models import Llama, Lion, Horse, Goat, Elephant, Dolphin, Octopus, Seahorse, Shark, Whale, Lizard, Snail, Snake, Spider, Worm, PettingZoo, SnakePit, Wetlands

def create_attractions_with_animals():
    varmint_village = PettingZoo("Varmint Village", "A place for cuddles")
    wet_place = Wetlands("Wet Place", "Wet & Gross")
    snake_sack = SnakePit("Snake Sack", "Slimy & Weird")


    tina = Llama("Tina", "fat lard", "morning", "Llama Chow")
    aslan = Lion("Aslan", "huge", "afternoon", "meat")
    harriet = Horse("Harriet", "racing", "afternoon", "grass")
    lawrence = Goat("Lawrence", "fainting", "midday", "straw")
    steve = Elephant("Steve", "white", "morning", "trees")
    varmint_village.add_animals(tina)
    varmint_village.add_animals(aslan)
    varmint_village.add_animals(harriet)
    varmint_village.add_animals(lawrence)
    varmint_village.add_animals(steve)


    joe = Dolphin("Joe", "baiji", "morning", "fishies")
    larry = Octopus("Larry", "cyanea", "morning", "ink")
    gary = Seahorse("Gary", "baiji", "morning", "plankton")
    jerry = Shark("Jerry", "great white", "afternoon", "human leg")
    bob = Whale("Bob", "sea", "midday", "bubbles")
    wet_place.add_animals(joe)
    wet_place.add_animals(larry)
    wet_place.add_animals(gary)
    wet_place.add_animals(jerry)
    wet_place.add_animals(bob)


    gilbert = Lizard("Gilbert", "shiny", "midday", "ants")
    sam = Snail("Sam", "slow", "afternoon", "slime")
    sawyer = Snake("Sawyer", "sthnake", "afternoon", "rat")
    satan = Spider("Satan", "scary & gross", "afternoon", "nothing")
    wilbur = Worm("Wilbur", "sticky", "morning", "little worms")
    snake_sack.add_animals(gilbert)
    snake_sack.add_animals(sam)
    snake_sack.add_animals(sawyer)
    snake_sack.add_animals(satan)
    snake_sack.add_animals(wilbur)

    return varmint_village, wet_place, snake_sack
