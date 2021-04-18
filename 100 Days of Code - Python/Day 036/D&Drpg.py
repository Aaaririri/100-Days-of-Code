import requests
import json
# https://www.dnd5eapi.co/docs/
api = "https://www.dnd5eapi.co"
api_aux = "https://www.dnd5eapi.co/api/weapon-properties"
with open("Day 036/D&Drpg.json", "r") as data:
    endpoints = json.load(data)

for items, ends in endpoints.items():
    response = requests.get(api + ends)
    response.raise_for_status()
    response = response.json()
    print(response)
    print("----------------------------------------------------------------")
    response = response["results"]
    for i in range(len(response) - 1):
        for names, results in response[i].items():
            print(results)
