from datetime import date

class Llama:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.walking = True
        self.date_added = date.today()


class Horse:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.walking = True
        self.date_added = date.today()


class Goat:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.walking = True
        self.date_added = date.today()


class Lion:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.walking = True
        self.date_added = date.today()


class Elephant:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.walking = True
        self.date_added = date.today()


class Lizard:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.slithering = True
        self.date_added = date.today()


class Snake:
    
    def __init__(self):
        self.name = ""
        self.species = ""
        self.slithering = True
        self.date_added = date.today()


class Spider:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.slithering = True
        self.date_added = date.today()


class Worm:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.slithering = True
        self.date_added = date.today()


class Snail:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.slithering = True
        self.date_added = date.today()


class Shark:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.swimming = True
        self.date_added = date.today()


class Whale:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.swimming = True
        self.date_added = date.today()


class Octopus:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.swimming = True
        self.date_added = date.today()


class Seahorse:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.swimming = True
        self.date_added = date.today()


class Dolphin:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.swimming = True
        self.date_added = date.today()


def main():
    joe = Dolphin()
    joe.name = "Joe"
    joe.species = "Baiji"
    print(f'{joe.name}! Species: {joe.species} | Is {joe.name} swimming? {joe.swimming}! When was he added? {joe.date_added}')
