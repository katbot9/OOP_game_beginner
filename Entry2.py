from textwrap import dedent

class Entry2():
    def enter(self):
        print(dedent("""
        After cutting the monster's head, you notice a wooden door behind his corpse,
        you enter the door and another monster surprises you by a sword attack.
        What is your next move.
        """))

        move = input("> ")

        if move == "dodge":
            print(dedent("""
                You try to dodge his sword but it was too late so he cuts your right
                arm off. You have no sword to fight back so you try to run away desperately.
                you get to the closed way left because of the explosion, you bow down and start
                crying and screaming with fear.
                The monster doesn't care, he cuts your head, and puts it in a bag to bring it
                to his children.
                """
            ))

            return 'death'

        elif move == 'parry':
            print(dedent("""
                Your inhuman reflexes allow you to think rapidly and parry the monster, the beast
                is so shocked that he stands still, you swing with your sword and cut both his arms,
                then remove his head with a rapid sword attack.
            """))

            return 'entry3'

        else:
            print("DOES NOT COMPUTE!")
            return 'entry2'
