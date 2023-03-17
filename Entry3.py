from textwrap import dedent
from random import randint

class Entry3():
    def enter(self):
        print(dedent("""
            You're so tired but you have to find the treasure at all costs,
            so you carry on your way and find a weird door, as you get closer
            you notice a bar where you have to enter a secret code composed of
            3 numbers. You only have 10 tries!!
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(code)
        number = 0

        while number < 9:
            guess = input("> ")
            if guess != code:
                print("bzzzt, wrong code")
            else:
                return 'finished'
        return 'death'
