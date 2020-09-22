#!/usr/bin/env python3
hostname = input("What value should we set for hostname? ")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname == "mtg":  # hostname input matches string and case
    print("hostname matches expected config")
elif hostname.lower() == "mtg": # hostname input matches string.lower()
    print("The hostname was found to be mtg")
else:
    print("The hostname is invalid")
print("Exiting the script")
