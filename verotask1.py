# Source: https://www.youtube.com/watch?v=HHKZmafFExM
# https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
import requests
import csv
import json

api_key = 'not having for now'

req = requests.get('https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active')
url_content = req.content
csv_file = open('downloaded1.json', 'wb')


csv_file.write(url_content)
# Take the Vehicles.csv

def make_json(csvFilePath, jsonFilePath, csv_file):
     
    # create a dictionary
    data = {}
    header_data = []
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        entries = csvReader
        for entry in entries:
            for item in entry:
                header_data = [x for x in item.split(";")]
                print(header_data)
            # Assuming a column named 'No' to
            # be the primary key
            #print(entry)

 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         
# Driver Code
 
# Decide the two file paths according to your
# computer system
csvFilePath = r'vehicles.csv'
jsonFilePath = r'csvtojson.json'
 
# # Call the make_json function
make_json(csvFilePath, jsonFilePath, csv_file)
csv_file.close()
