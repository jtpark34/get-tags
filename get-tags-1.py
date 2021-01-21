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
sys.stdout = open("output.txt", "wt")

for url in links:
    response = requests.get(url)
    data = response.json()

    for i in data['items']:
        print(i['name'])

sys.stdout.close()
sys.stdout=orig_stdout

with open('output.txt') as f:
    count = 0
    for line in f:
        count += 1

print(f"There are {count} tags. \nCheck output.txt to view your results.")
