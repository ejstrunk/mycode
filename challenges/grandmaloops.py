#!/usr/bin/env python3


def counter():
    biscuits = ["room", "kitchen", "bathroom", "room", "living room", "room"]
    print("Grandma: For every biscuit I find in your room, I'm going to flog you!\n")
    biscuit = 0
    for i in biscuits:
        if i == "room":
            biscuit = biscuit + 1
            print(f"Grandma flogs you {biscuit} time(s)!")

def delete():
    toys = [{"hallway": ["power ranger", "transformer", "marbles"], "legos"]
    print("\nGrandma: For every toy I find in the hallway, I'm going to throw them away!\n\nGrandma threw away...")
    for i in toys:
        print(f"... your {i}!")

def add():
    reportcard = ["A", "B", "A", "C", "A", "B"]
    videogames = 0
    print("Grandma: For every \"A\" I find in your report card, I'm going to give you a new video game for your collection")
    for i in reportcard:
        if i == "A":
            videogames = videogames + 1
    print(f"Grandma gave you {videogames} new video game(s)!")

counter()
delete()
add()
