import csv as csv

with open('prueba.csv', newline='') as File:  
    reader = csv.DictReader(File)
    for row in reader:
        print(row['unico'])