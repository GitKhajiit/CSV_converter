import csv

with open('CSV_files/36.csv', 'r', newline='') as csvfile:
    filereader = csv.reader((line.replace('\0', '') for line in csvfile), delimiter=' ')
    for i in filereader:
        if len(i) == 0:
            pass
        else:
            print(i[0])
