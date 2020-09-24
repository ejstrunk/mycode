#!/usr/bin/env python3

import sys

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

print("On our NE Farm, we raise:")
for i in farms[0]['agriculture']:
    print(i)

selection = input("Please select NE Farm, W Farm, or SE Farm:\n>>>>").lower()
while selection != "q":
    if selection == "ne farm":
        print("On the NE Farm we have: ")
        for i in farms[0]['agriculture']:
            print(i)
        break
    elif selection == "w farm":
        print("On the W Farm we have:")
        for i in farms[1]['agriculture']:
            print(i)
        break
    elif selection == "se farm":
        print("On the SE Farm we have:")
        for i in farms[2]['agriculture']:
            print(i)
        break
    elif selection == "q":
        print("Goodbye")
        sys.exit()
    else:
        print("Incorrect choice. Try again or type \"q\" to exit.")
        continue

selectionanimals = input("Please select NE Farm, W Farm, or SE Farm to view the animals we raise there:\n>>>").lower()
if selectionanimals == "ne farm":
    print("On the NE Farm we have: ")
    for i in farms[0]['agriculture']:
        if i in animals:
            print(i)
elif selectionanimals == "w farm":
    print("On the W Farm we have:")
    for i in farms[1]['agriculture']:
        if i in animals:
            print(i)
elif selectionanimals == "se farm":
    print("On the SE Farm we have:")
    for i in farms[2]['agriculture']:
        if i in animals:
            print(i)
