import csv

fileObj = open("cities.csv")
csvObj = csv.DictReader(fileObj)

for row in csvObj:
    print(type(row))
    print(row)