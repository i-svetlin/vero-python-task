# Source: https://www.youtube.com/watch?v=HHKZmafFExM
import requests
import csv

api_key = 'not having for now'

req = requests.get('https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active')
url_content = req.content
csv_file = open('downloaded1.json', 'wb')
csv_file.write(url_content)
csv_file.close()