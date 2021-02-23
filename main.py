import csv
import os

files_list = os.listdir('CSV_files')
files_count = len(files_list)
list = [[] for x in range(files_count)]

i = 0
for file in files_list:
    with open(f'CSV_files/{file}', 'r') as csv_file:
        csv_reader = csv.reader(x.replace('\0', '') for x in csv_file)
        for row in csv_reader:
            try:
                list[i].append(row[0])
            except IndexError:
                pass
    i += 1

print(list)
