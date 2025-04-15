"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *


def main():
    """
    TODO:Sinny
    """
    pass
    for i in range(3):
        go_in()
        put_beeper99()
        go_out()

def go_in():
    """
    pre_condition:Karel is at the upper lef of the pothole,facing East
    post_condition:Karel is in the pothole,facing North
    """
    move()
    turn_right()
    move()
    turn_right()
    turn_right()

def go_out():
    """
    pre_condition:Karel is in the pothole,facing North
    post_condition:Karel is at the upper lef of the pothole,facing East
    """
    move()
    turn_right()
    move()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
