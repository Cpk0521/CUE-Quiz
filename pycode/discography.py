import json

discolist = [
    [0, '/', '/', '/', 0, ['CD_Blank.png'], ""],
    [1, '2019-08-09', 'CUE! 00 Limited Mini Album', 'See you everyday', 1, ['MA00.jpg'], ""],
    [2, '2019-11-27', 'CUE! 01 Single', 'Forever Friends', 3, ['S01_1.png', 'S01_2.png'], "https://lnk.to/foreverfriends"],
    [3, '2020-01-22', 'CUE! Team Single 01', 'Knocking on My Dream!!', 4, ['TS01.jpg'], "https://lnk.to/CUE_TeamSingle01"],
    [4, '2020-01-22', 'CUE! Team Single 02', 'にこにこワクワク 最高潮！', 4, ['TS02.jpg'], "https://lnk.to/CUE_TeamSingle02"],
    [5, '2020-01-22', 'CUE! Team Single 03', 'Good meal, Good life', 4, ['TS03.jpg'], "https://lnk.to/CUE_TeamSingle03"],
    [6, '2020-01-22', 'CUE! Team Single 04', 'MiRAGE! MiRAGE!!', 4, ['TS04.jpg'], 'https://lnk.to/CUE_TeamSingle04'],
    [7, '2020-03-25', 'CUE! 02 Single', 'beautiful tomorrow', 3, ['S02_1.png', 'S02_2.png'], 'https://lnk.to/beautifultomorrow'],
    [8, '2020-08-26', 'CUE! 03 Single', 'Colorful／カレイドスコープ', 3, ['S03_1.png', 'S03_2.png'], 'https://lnk.to/ColorfulKaleidoscope'],
    [9, '2020-09-16', 'CUE! Team Single 05', 'Reach For The World!', 4, ['TS05.png'], 'https://lnk.to/CUE_TeamSingle05'],
    [10, '2020-09-16', 'CUE! Team Single 06', 'NAZO-NAZE Jumping!', 4, ['TS06.png'], 'https://lnk.to/CUE_TeamSingle06'],
    [11, '2020-09-16', 'CUE! Team Single 07', 'Red or Blue？', 4, ['TS07.png'], 'https://lnk.to/CUE_TeamSingle07'],
    [12, '2020-09-16', 'CUE! Team Single 08', 'Override!', 4, ['TS08.png'], 'https://lnk.to/CUE_TeamSingle08'],
    [13, '2021-01-06', 'CUE! 04 Single', '最高の魔法', 3, ['S04_1.jpg', 'S04_2.jpg'], 'https://lnk.to/SaikonoMahoPC'],
    [14, '2021-04-21', 'CUE! 01 Album', 'Talk about everything', 2, ['A01_1.jpg', 'A01_2.jpg'], 'https://lnk.to/Talk_about_everything'],
    [15, '2022-1-26', '主題歌CD', 'スタートライン／はじまりの鐘の音が鳴り響く空', 3, ['oped_jk.jpg', 'oped_jk_syokai.jpg'], 'https://lnk.to/CUE05'],
]

discoTypes = [
    [0, 'Not on sale'], [1, 'Mini Album'], [2, 'Album'], [3, 'Single'], [4, 'Team Single']
]

jsondata = {'discolist':[], 'discoTypes':[]}

for disco in discolist:
    dicojson = {'id':disco[0], 'date':disco[1], 'type':disco[4] ,'title':disco[2], 'name':disco[3], 'cover':[], 'lnkto':disco[6]}
    for img in disco[5]:
        dicojson['cover'].append({'file':img})
    jsondata['discolist'].append(dicojson)

for dtype in discoTypes:
    jsondata['discoTypes'].append({'id':dtype[0], 'typename':dtype[1]})

with open('discography.json', 'w', encoding='utf-8') as outfile:
    json.dump(jsondata, outfile, indent=4, ensure_ascii=False)