"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    pre_condition:Karel is on the lefe side of the wall, facing East
    post_condition:Karel is on the right side of the wall
    """
    up()
    cross()
    down()


def cross():
    """
    post_condition:Karel is at the upper left of the wall, facing North
    post_condition:Karel is at the upper right, facing South
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    pre_condition:Karel is at the upper right, facing South
    post_condition:Karel is at the downer , facing East
    """
    while front_is_clear():
        move()


def up():
    """
       pre_condition:Karel is on the lefe side of the wall, facing East
       post_condition:Karel is at the upper left of the wall, facing North
    """
    turn_left()
    while not right_is_clear():
        move()
    # alternative:
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()



def turn_right():
    turn_left()
    turn_left()
    turn_left()





# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
