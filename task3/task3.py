import json
import sys

with open(sys.argv[1], 'r') as tests:
    tests = json.load(tests)
    
with open(sys.argv[2], 'r') as values:
    values = json.load(values)['values']

# Func that searches and returns particular test value (or '') based on test id, then removes that test data from list

def values_search(id):
    for i in range(len(values)):
        if 'id' in values[i] and values[i]['id'] == id:
            value = values[i]['value']
            values.pop(i)
            return value
    else:
        return ''
    
# Func that scans tests tree and updates values

def tests_search_update(data):
    for j in data:
        if 'id' in j:
            j['value'] = values_search(j['id'])
        if 'values' in j:
            tests_search_update(j['values'])
            
tests_search_update(tests['tests'])
with open('report.json', 'w') as outfile:
    json.dump(tests, outfile)
