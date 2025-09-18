#Bahopiya Dhaval

import csv
with open(r'C:\Users\student\Downloads\data-1 (2).csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
