import json
 
# Opening JSON file
f = open(r'path')
 
# returns JSON object as
# a dictionary
data = json.load(f)
dicti = {}
for key, val in data['Info'].items():
    dicti[key] = val
[print(key, ":", val) for key, val in dicti.items()]
# Closing file
f.close()
