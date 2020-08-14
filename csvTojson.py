import csv, json

csvpath = 'testrecord.csv'
jsonpath = 'jsonrecord.json'

colsname = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 
            'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 
                'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']
data = {}
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    i = 0
    for row in csvreader:
        data[colsname[i]] = row[0]
        i = i + 1

with open(jsonpath,'w') as jsonfile:
    jsonfile.write(json.dumps(data, indent=4))