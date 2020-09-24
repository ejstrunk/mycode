#!/usr/bin/env python3

import requests

astro_api = "http://api.open-notify.org/astros.json"

astros = requests.get(astro_api).json()

print(f"People in space: {astros['number']}")

for i in astros['people']:
    print(f"{i['name']} on the {i['craft']}")
