import json

with open('maintenance.json') as json_file:
    d = json.load(json_file)
    for aes in d['accountingEntity']:
        print(aes['AE'])