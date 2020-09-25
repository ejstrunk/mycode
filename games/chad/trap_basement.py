#!/usr/bin/env python3
import sys

""" Basement Trap (a la Star Wars Trash Compactor)
    by Everett J Strunk"""
print("""COOL INTRO AND ASCII BORDER GOES HERE""")


# player takes first step into basement, stairs flatten into slide, player ends up in timed trap with walls closing
# timer based on number of actions. Timer runs out == death

# main code in trap()

def trap():
    while True:
        timer = 6
        actions = 6
        user_input = input("Testing action function: press y ").lower()
        if user_input == "y":
            use_action(timer, actions)
            print(f"Timer: {timer}, Actions: {actions}")
            continue
        elif user_input == "q":
            sys.exit()
        else:
            continue


def use_action(timer, actions):
    timer -= 1
    actions -= 1
    return timer, actions


trap()
