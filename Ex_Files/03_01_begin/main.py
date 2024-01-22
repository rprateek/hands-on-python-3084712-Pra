import csv
from datetime import datetime
from pprint import pprint


with open("laureates.csv", "r") as f:
    contents = csv.DictReader(f)
    lstContents = list(contents)

for content in lstContents:
    if content["surname"] == "Einstein":
        pprint(content)
        pprint("==========")
        year_date = datetime.strptime(content["year"], "%Y")
        born_date = datetime.strptime(content["born"], "%Y-%m-%d")
        print("age:", year_date.year- born_date.year)
        break
