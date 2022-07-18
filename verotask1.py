# Source: https://www.youtube.com/watch?v=HHKZmafFExM
# https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
import csv
import json
import requests
#import pandas as pd

api_key = 'not having for now'

req = requests.get('https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active')
url_content = req.content
csv_file = open('downloaded2.json', 'wb')


csv_file.write(url_content)
# Take the Vehicles.csv

def make_json(csv_file_path, json_file_path, csv_file):
    tocsvrows = [] 
    # create a dictionary
    data = {}
    header_data = []
    with open(csv_file_path, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        counter = 0
        entries = csvReader
        #print(f'header entries: {entries}')
        for entry in entries:
            for item in entry:
                if item:
                    if counter < 1:
                        header_data = [x for x in item.split(";")]
                        counter += 1 
                    tocsvrows.append(entry['gruppe;kurzname;langtext;info;lagerort;labelIds'].split(';'))
        f = open('./newfile.csv', 'w')
# create the csv writer
        writer = csv.writer(f, delimiter=';')            
        #writer = csv.DictWriter(f, delimiter=';')            
        #writer.writeheader(header_data)  
        writer.writerow(header_data)  
        writer.writerows(tocsvrows)  
    with open(csv_file_path, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            for head in header_data:
                key = rows[head]
                data[key] = rows
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

csv_file_path = r'vehicles.csv'
json_file_path = r'csvtojson.json'

 
# Call the make_json function
make_json(csv_file_path, json_file_path, csv_file)



csv_file.close()


