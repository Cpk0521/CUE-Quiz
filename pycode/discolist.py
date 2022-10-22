import json

#   id | date | title | CDname | cover
discolist = [
    [0, '/', '/', '/', 0, ['CD_Blank.png'], ""],
    [1, '2019-08-09', 'CUE! 00 Limited Mini Album', 'See you everyday', ['MA00.jpg'], ""],
    [2, '2019-11-27', 'CUE! 01 Single', 'Forever Friends', ['S01_1.png', 'S01_2.png'], "https://lnk.to/foreverfriends"],
    [3, '2020-01-22', 'CUE! Team Single 01', 'Knocking on My Dream!!', ['TS01.jpg'], "https://lnk.to/CUE_TeamSingle01"],
    [4, '2020-01-22', 'CUE! Team Single 02', 'にこにこワクワク 最高潮！', ['TS02.jpg'], "https://lnk.to/CUE_TeamSingle02"],
    [5, '2020-01-22', 'CUE! Team Single 03', 'Good meal, Good life', ['TS03.jpg'], "https://lnk.to/CUE_TeamSingle03"],
    [6, '2020-01-22', 'CUE! Team Single 04', 'MiRAGE! MiRAGE!!', ['TS04.jpg'], 'https://lnk.to/CUE_TeamSingle04'],
    [7, '2020-03-25', 'CUE! 02 Single', 'beautiful tomorrow', ['S02_1.png', 'S02_2.png'], 'https://lnk.to/beautifultomorrow'],
    [8, '2020-08-26', 'CUE! 03 Single', 'Colorful／カレイドスコープ', ['S03_1.png', 'S03_2.png'], 'https://lnk.to/ColorfulKaleidoscope'],
    [9, '2020-09-16', 'CUE! Team Single 05', 'Reach For The World!', ['TS05.png'], 'https://lnk.to/CUE_TeamSingle05'],
    [10, '2020-09-16', 'CUE! Team Single 06', 'NAZO-NAZE Jumping!', ['TS06.png'], 'https://lnk.to/CUE_TeamSingle06'],
    [11, '2020-09-16', 'CUE! Team Single 07', 'Red or Blue？', ['TS07.png'], 'https://lnk.to/CUE_TeamSingle07'],
    [12, '2020-09-16', 'CUE! Team Single 08', 'Override!', ['TS08.png'], 'https://lnk.to/CUE_TeamSingle08'],
    [13, '2021-01-06', 'CUE! 04 Single', '最高の魔法', ['S04_1.jpg', 'S04_2.jpg'], 'https://lnk.to/SaikonoMahoPC'],
    [14, '2021-04-21', 'CUE! 01 Album', 'Talk about everything', ['A01_1.jpg', 'A01_2.jpg'], 'https://lnk.to/Talk_about_everything'],
    [15, '2022-1-26', '主題歌CD', 'スタートライン／はじまりの鐘の音が鳴り響く空', ['oped_jk.jpg', 'oped_jk_syokai.jpg'], 'https://lnk.to/CUE05'],
    [16, '2022-5-18', '2クール目主題歌CD', 'Tomorrow\'s Diary／ゆめだより', ['oped2_jk_normal.jpg', 'oped2_jk_syokai.jpg'], 'https://lnk.to/CUE06'],
    [17, '2022-3-16', '', 'Blu-ray 第6巻', ['bd_1_jk.jpg'], 'https://cue-animation.jp/product/bd/bd_1/'],
    [18, '2022-4-20', '', 'Blu-ray 第6巻', ['bd_2_jk.jpg'], 'https://cue-animation.jp/product/bd/bd_2/'],
    [19, '2022-5-18', '', 'Blu-ray 第6巻', ['bd_3_jk.jpg'], 'https://cue-animation.jp/product/bd/bd_3/'],
    [20, '2022-6-15', '', 'Blu-ray 第6巻', ['bd_4_jk.jpg'], 'https://cue-animation.jp/product/bd/bd_4/'],
    [21, '2022-7-20', '', 'Blu-ray 第6巻', ['bd_5_jk.jpg'], 'https://cue-animation.jp/product/bd/bd_5/'],
    [22, '2022-8-17', '', 'Blu-ray 第6巻', ['bd_6_jk.jpg'], 'https://cue-animation.jp/product/bd/bd_6/'],
    [23, '2022-11-16', 'CUE! Limited Mini Album', '花鳥風月', ['CUE_miniAL_jk_RGB.jpg'], ''],
]

#   id | name | disco | audio | link | optionshow
audiolist = []

audiotype = [
    [1, 'Normal'],
    [2, 'Instrumental'], 
    [3, 'Team'],
    [4, 'Solo']
]

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