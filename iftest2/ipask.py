#!/usr/bin/env python3

ipchk = input("Apply an IP address: ") # this line now promts the user for input

# a provided string will test true
if ipchk:
    print(f"Looks like the IP address was set: {ipchk}")
else: # if data is NOT provided
    print("You did not provide an input.")
