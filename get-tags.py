import json
import requests
import sys

keyID = "keyID"

links = [f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=1',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=2',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=3',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=4',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=5',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=6',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=7',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=8',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=9',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=10',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=11',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=12',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=13',
f'https://linkedin.stackenterprise.co/api/2.2/tags?key={keyID}((&pagesize=100&page=14']

orig_stdout = sys.stdout
sys.stdout = open("output.txt", "wt") # creates and opens file, and records output

for url in links: # loops through array
    response = requests.get(url) # stores GET requests to the API as a variable
    data = response.json() # stores the JSON responses as a variable

    for i in data['items']: # loops through nested dictionary in JSON responses
        print(i['name']) # prints value for key "name"

sys.stdout.close() # closes file
sys.stdout=orig_stdout

with open('output.txt') as f: 
    count = 0 # sets initial count as zero
    for line in f: # loops through output.txt file
        count += 1 # counts each line in the file (count = count + 1) and stores as a variable

print(f"There are {count} tags. \nCheck output.txt to view your results.") # prints formatted string with total count and prompts user to check output file.
