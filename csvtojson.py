import csv 
import json
import time
import pandas as pd

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            for (k, v) in row.items():
                try:
                    if k:
                        data_header_item = k.split(';')
                except:
                    pass
                try:
                    if v:
                        data_item = v.split(';')
                except:
                    pass

                if len(data_header_item) == len(data_header_item):
                    arr_appendable = dict(zip(data_header_item, data_item))
                    jsonArray.append(arr_appendable)
    #convert python jsonArray to JSON String and write to file
        df = pd.DataFrame(jsonArray)
        print(df)
        
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
        
csvFilePath = r'vehicles.csv'
jsonFilePath = r'vehicles.json'

start = time.perf_counter()
csv_to_json(csvFilePath, jsonFilePath)
finish = time.perf_counter()

