#!/usr/bin/python
import requests as req
import datetime
import argparse
import pandas as pd

import csv
from requests.api import head



parser = argparse.ArgumentParser()

#f = open('./vehicles.csv', 'w')

link = "https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active"
response = req.get(link)
fox = (response.json()) #TODO: Fix fox to correspond to CSV file
#writer = csv.writer(f)

with req.get(fox) as rq: # make it use csv file
    with open('test.csv', 'wb') as file:
        pd.read_csv(rq.content)

        #file.write(rq.content) 

#     #with open('test.csv', 'w') as f:
#     # create the csv writer
#     writer = csv.writer(rq.content)

# # write a row to the csv file
#     writer.writerow(rq.content)

# #print(fox)
# with open('response.csv', 'w', newline='') as csvfile:
#     fieldnames = ['name', 'city', 'Height']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     for row in responsejson:
#         writer.writerow(row)