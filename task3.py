import json

ValuesAddr, TestsAddr = input(), input()

with open(ValuesAddr, 'r') as values:
    values = json.load(values)['values']


with open(TestsAddr, 'r') as tests:
    tests = json.load(tests)

# Func that searches and returns particular test value (or '') based on test id, then removes that test data from list

def ValuesSearch(id):
    for i in range(len(values)):
        if 'id' in values[i] and values[i]['id'] == id:
            value = values[i]['value']
            values.pop(i)
            return value
    else:
        return ''
    
# Func that scans tests tree and updates values

def TestsSearchUpdate(data):
    for j in data:
        if 'id' in j:
            j['value'] = ValuesSearch(j['id'])
        if 'values' in j:
            TestsSearchUpdate(j['values'])
            
TestsSearchUpdate(tests['tests'])
with open('report.json', 'w') as outfile:
    json.dump(tests, outfile)