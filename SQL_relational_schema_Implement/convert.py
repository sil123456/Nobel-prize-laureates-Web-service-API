import json

# load data
data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))

# get the id, givenName, and familyName of the first laureate

# id = laureate["id"]
# givenName = laureate["givenName"]["en"]
# familyName = laureate["familyName"]["en"]


laureates = data["laureates"]
LAUREATE = dict()
f1 = open('Laureates.del', 'w')

# for item in laureates:
#     lst = []
#     if item.keys() not in lst:
#         lst.append(item.keys())
#     else:
#         continue
#     # #print(item)
#     # id = item['id']
#     print(lst)


for item in laureates:
    id = item['id']
    familyName = r'\N'
    givenName = r'\N'
    gender = r'\N'
    birth = r'\N'
    date = r''
    place = r'\N'
    city = r'\N'
    country = r'\N'

    cat1 = ['givenName', 'orgName']
    for name1 in cat1:
        if name1 not in item:
            pass
            #print('Error! Wrong Orgnization name')
        else:
            TYPE = '"' + item[name1]['en'] + '"'

    cat2 = ['birth', 'founded']
    for name2 in cat2:
        if name2 not in item:
            pass
            #print('Error! basic information name')
        else:
            if 'date' in item[name2]:
                date = item[name2]['date'].replace('-','')
            if 'place' in item[name2]:
                place = item[name2]['place']
                if 'city' in place:
                    city = '"' + place['city']['en'] + '"'
                if 'city' in place and 'country' in place:
                    country = '"' + place['country']['en'] + '"'
    
    if 'familyName' in item:
        familyName = '"' + item['familyName']['en'] + '"'
    if 'givenName' in item:
        givenName = '"' + item['givenName']['en'] + '"'
    if 'gender' in item:
        gender = '"' + item['gender'] + '"'

    lst = [id, TYPE, familyName, gender, date, city, country]
    if id not in LAUREATE:
        line = ','.join(lst) + '\n'
        f1.write(line)
        #LAUREATE[id] = True

f1.close()
# print the extracted information
#print(id + "\t" + givenName + "\t" + familyName)

FLAGN = 1
FLAGA = 1
f2 = open('NobelPrizes.del', 'w')
f3 = open('Affiliations.del', 'w')
for item in laureates:

    id = item['id']
    awardYear = r'\N'
    category = r'\N'
    sortOrder = r'\N'
    #affiliations = r'\N'
    name = r'\N'
    city = r'\N'
    country = r'\N'

    nobelPrizes = item['nobelPrizes']
    for item2 in nobelPrizes:
        if 'awardYear' in item2:
            awardYear = item2['awardYear']
        if 'category' in item2:
            category = '"' + item2['category']['en'] + '"'
        if 'sortOrder' in item2:
            sortOrder = item2['sortOrder']

        # awardYear = item2['awardYear']
        # category = '"' + item2['category']['en'] + '"'
        # sortOrder = item2['sortOrder']

        lst1 = [id, awardYear, category, sortOrder, str(FLAGN)]
        line1 = ','.join(lst1) + '\n'
        f2.write(line1)

    

        if 'affiliations' not in item2:
            #print('zai')
            affiliations = r'\N'
        elif 'affiliations' in item2:
            affiliations = item2['affiliations']

            for item3 in affiliations:
                if 'name' in item3:
                    name = '"' + item3['name']['en'] + '"'
                if 'city' in item3:
                    city = '"' + item3['city']['en'] + '"'
                if 'city' in item3 and 'country' in item3:
                    country = '"' + item3['country']['en'] + '"'

                lst2 = [id, name, city, country, str(FLAGN), str(FLAGA)]
                line2 = ','.join(lst2) + '\n'
                f3.write(line2)
                FLAGA += 1
        FLAGN += 1


f2.close()
f3.close()












