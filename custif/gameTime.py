#!/usr/bin/env python3

import time
import sys

location = {"entry": {"north": "dining room", "east": "living room", "up": "loft"
        },
        "living room": {"north": "kitchen", "west": "entry"
        },
        "kitchen": {"south": "living room", "west": "dining room"
        },
        "dining room": {"east": "kitchen", "north": "backyard", "south": "entry"
        },
    "backyard": {
        },
    "loft": {"down": "entry", "east": "master bedroom", "north": "office", "northeast": "spare bedroom"
        },
    "master bedroom": {
        },
    "spare bedroom": {
        },
    "office": {
        }
    }
inventory = ["flashlight"]
move = " "
current_room = "entry"

def main():
    print("""()()()()()-------------------------------------------()()()()()
()()()()()|                  The                    |()()()()()
()()()()()|                Haunted                  |()()()()()
()()()()()|                 House                   |()()()()()
()()()()()-------------------------------------------()()()()()
             """)
    ## text intro
    move = input("You find yourself in the dimly lit entryway of a small two-story home.\nArmed with only a flashlight, you see that you can move north into a dining room, east into a living room, or upstairs.\nYou may type \"q\" at any time to exit the game.\nWhere would you like to go?\n>").lower
    ## entry while loop
    while move != "q":
        current_room = "entry"
        if move in location[{current_room}]:
            current_room = move
            print(f"You are now in the {current_room}")
            return current_room
            continue
        else:
            move = input("Please select a valid direction.\n>")
            continue
    print("Thank you for playing. Goodbye")
    sys.exit()
        
main()
