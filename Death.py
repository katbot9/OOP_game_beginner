from sys import exit
from random import randint

class Death():

    quips = [
    "You died. You kinda suck at this.",
    "Your mom would be proud...if she were smarter",
    "Such a luser.",
    "I have a small puppy that's better at this.",
    "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)
