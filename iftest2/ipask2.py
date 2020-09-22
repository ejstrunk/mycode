#!/usr/bin/env python3

import ipaddress 
ipchk = input("Apply an IP address: ")
if ipaddress.ip_address(ipchk):

# if user set IP of gateway
# if ipchk == "192.168.70.1":
  # print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
# elif ipchk: # if any data is provided, this will test true
   #print("Looks like the IP address was set: " + ipchk) # indented under if
#else: # if data is NOT provided
   #print("You did not provide input.") # indented under else

# if user set IP at all
    if ipchk == "192.168.70.1":
        print(f"Looks like the IP address of the Gateway was set: {ipchk}\nThis is not recommended")
    else:
        print(f"Looks like the IP address was set: {ipchk}")
else:
    print("Invalid IP address")
