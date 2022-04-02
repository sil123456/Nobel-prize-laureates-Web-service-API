import json

# load data
data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))

# get the id, givenName, and familyName of the first laureate
laureate = data["laureates"]
f = open('laureates.import', 'w')
for item in laureate:
    f.write(json.dumps(item))
f.close()



