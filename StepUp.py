"""
File: StepUp.py
Name: Sinny
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


def main():
    # algorithm
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper99()
    move()

def turn_right():
    """
    pre_condition:Karel is facing North
    post_condition:Karel is facing East
    """
    for i in range(3):
        turn_left()

def put_beeper99():
    """
    pre_condition:Karel在牆上，且拿著一顆球
    post_condition:Karel牆上，身下有九十九顆球
    """
    for i in range(99):
        put_beeper()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
