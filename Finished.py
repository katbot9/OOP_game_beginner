from textwrap import dedent
class Finished():
    def enter(self):
        print(dedent("""
            You did it! you've finally made it to the treasure room!
            You won!
            """))
        return 'finished'
