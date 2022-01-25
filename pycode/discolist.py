import json


#   id | title | name | cover
discolist = []

#   id | name | disco | audio | link | optionshow
audiolist = []

jsondata = {'discolist':[], 'Songs':[]}

for disco in discolist:
    discojson = {'id':disco[0], 'title':disco[1], 'name':disco[2], 'cover':[]}
    for img in disco[3]:
        discojson['cover'].append({'file':img})
    jsondata['discolist'].append(discojson)

for song in audiolist:
    songjson = {'id':song[0], 'name':song[1], 'discos':[], 'audio':song[3], 'link':[], 'optshow':song[5]}
    for disco in song[2]:
        songjson['discos'].append({'disco':disco})
    for no in song[4]:
        songjson['link'].append({'id':no})
    jsondata['Songs'].append(songjson)

with open('DataList.json', 'w', encoding='utf-8') as outfile:
    json.dump(jsondata, outfile, indent=4, ensure_ascii=False)