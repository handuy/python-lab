import csv

fileObj = open("addresses.csv", "w", newline="")
csvObj = csv.writer(fileObj)

csvObj.writerow(["Duy", "Tyler", "7452 Terrace 'At the Plaza' road", "SomeTown", "SD", 91234])

fileObj.close()