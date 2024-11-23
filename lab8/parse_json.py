#!/usr/bin/env python3

import json

# Open the JSON file
with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

f = open('data/chacon.csv', 'a')
for d in data[:5]:
    line = d['name'] + "," + d['html_url'] + "," + d['updated_at'] + "," + d['visibility'] + "\n"
    f.writelines(line)
f.close()

 
