#!/usr/bin/python

import requests as req
import datetime
import argparse
# Getopt
import sys, getopt

parser = argparse.ArgumentParser()

parser.add_argument("-k", "--keys", type=str) 
parser.add_argument("-c", "--colored", type=bool default=True) 

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Input file is "'), inputfile
   print('Output file is "'), outputfile

if __name__ == "__main__":
   main(sys.argv[1:])

# https://www.tutorialspoint.com/python/python_command_line_arguments.htm

datetime.datetime.now().isoformat()

verolink = "https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active"
link = "http://randomfox.ca/floof"
response = req.get(link)
fox = (response.json())

with req.get(fox['image']) as rq:
    with open('my_pic.jpg', 'wb') as file:
        file.write(rq.content)

print(fox['image'])