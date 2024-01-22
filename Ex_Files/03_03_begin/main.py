import csv
import json
from pprint import pprint

EINSTEIN = {
     "birthplace": "England",
    "name": "David",
    "surname": "Beckham",
    "sport": "football",
    "age": 55,
}

einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
print(einstein_json)
pprint(back_to_dict)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
