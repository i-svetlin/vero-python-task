# Tutorial:
# https://www.youtube.com/watch?v=q5uM4VKywbA
import csv

with open('vehicles.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

    for line in csv_reader:
        del line['email']
        csv_writer.writerow(line)
        print(line)