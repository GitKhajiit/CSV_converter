import csv
import os

files_list = os.listdir('CSV_files')
files_count = len(files_list)
lists = [[] for x in range(files_count)]

i = 0
for file in files_list:
    with open(f'CSV_files/{file}', 'r', newline='') as csv_file:
        csv_reader = csv.reader((line.replace('\0', '') for line in csv_file), delimiter=' ')
        for row in csv_reader:
            try:
                lists[i].append(row)
            except IndexError:
                pass
    i += 1

with open('main.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';')
    for list in lists:
        for ex in list:
            csv_writer.writerow(list)

print(lists)
