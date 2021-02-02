import json
import requests
import sys

links = ['https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=1',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=2',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=3',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=4',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=5',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=6',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=7',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=8',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=9',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=10',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=11',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=12',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=13',
'https://linkedin.stackenterprise.co/api/2.2/tags?key=keyID((&pagesize=100&page=14']

orig_stdout = sys.stdout
sys.stdout = open("output.txt", "wt") # creates and opens file and records output

for url in links: # loops through array
    response = requests.get(url) # makes a GET request to the API and stores function as a variable
    data = response.json() # stores the json response as a variable

    for i in data['items']: # loops through nested dictionary
        print(i['name']) # prints value for key "name"

sys.stdout.close() # closes file
sys.stdout=orig_stdout

with open('output.txt') as f: 
    count = 0 # sets initial count as zero
    for line in f:
        count += 1 # counts each line in the file (count = count + 1) and stores as a variable

print(f"There are {count} tags. \nCheck output.txt to view your results.") # prints formatted string with total count and prompts user to check output file.
