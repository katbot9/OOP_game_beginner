from textwrap import dedent
class Entry1():
    def enter(selfdodg):
        print(dedent("""
            You enter into the dangerous dungeon that your whole village
            prevented you from going to because you're the main character,
            and ofcourse you won't die in the end and will figure a way out
            to defeat the final boss and get the treasure back home.
            As you open the door, you see a monster staring at you with angry
            eyes. You grab your legendary sword to fight back.
            He grabs an object and throws it into your diretcion.
            What is your next move?
            """))
        move = input("> ")

        if move == "cut the object":
            print(dedent("""
                You focus on the object to cut it into half, as it comes near your
                you try to cut the object with your legendary sword, but the object
                explodes mid-air and burns your face
                """))

            return 'death'

        elif move == "dodge":
            print(dedent("""
                you dodge the mysterious object with your quick moves and
                the object explodes behind you and ruins the way you came from,
                you realize that there is no coming back from this, so you rush into
                him rapidly that he barely notices you and you cut his head.
                """ ))
            return 'entry2'

        else:
            print("THIS DOES NOT COMPUTE!")
            return 'entry1'
