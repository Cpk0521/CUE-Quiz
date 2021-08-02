import json

songs = [
    ['Forever Friends', [1, 2, 14], 1, 'mB7THsrkBHc.mp3'],
    ['Forever Friends (Flower ver.)', [2], 3, 'czz8MR8HMY.mp3'],
    ['Forever Friends (Bird ver.)', [2], 3, 'DYFFBzewqug.mp3'],
    ['Forever Friends (Wind ver.)', [2], 3, '40xdAJyVT2c.mp3'],
    ['Forever Friends (Moon ver.)', [2], 3, '9YeMoi0TELY.mp3'],
    ['Forever Friends (Instrumental)', [2], 2, 'ILamWIhh4dE.mp3'],
    ['さよならレディーメイド', [2, 14], 1, 'jyElyIwQlT8.mp3'],
    ['さよならレディーメイド (Instrumental)', [2], 2, 'wjD0kW7yj8Y.mp3'],
    ['Knocking on My Dream!!', [1,3], 1, 'uTY2q0orDjQ.mp3'],
    ['Knocking on My Dream!! (Instrumental)', [3], 2, 'nq-u7qFRcO8.mp3'],
    ['One More Step!', [3], 1, '6dN0wXDcrZY.mp3'],
    ['One More Step! (Instrumental)', [3], 2, 'XqMavfj-arI.mp3'],
    ['にこにこワクワク 最高潮！', [4], 1, 'nAyhorybYvU.mp3'],
    ['にこにこワクワク 最高潮！ (Instrumental)', [4], 2, '1BqB14ode6Y.mp3'],
    ['ドリ☆アピ', [4], 1, 'Hvk0KHFhJ8I.mp3'],
    ['ドリ☆アピ (Instrumental)', [4], 2, 'mJUS_xE4SCg.mp3'],
    ['Good meal, Good life', [5], 1, 'Lva5atg7yDg.mp3'],
    ['Good meal, Good life (Instrumental)', [5], 2, 'dTEtbnS-bak.mp3'],
    ["Steppin' Girl", [5], 1, 'PCZ2U96vK3M.mp3'],
    ["Steppin' Girl (Instrumental)", [5], 2, 'JGN7dSRUAGM.mp3'],
    ['MiRAGE! MiRAGE!!', [6], 1, 'Pj8q4UxlvAk.mp3'],
    ['MiRAGE! MiRAGE!! (Instrumental)', [6], 2, 'kOwXl_Vn_pY.mp3'],
    ['ヒカリニ染マル未来', [6], 1, 'L_rl8cM5JrM.mp3'],
    ['ヒカリニ染マル未来 (Instrumental)', [6], 2, 'Z54gWWpm4Rs.mp3'],
    ['beautiful tomorrow', [7, 14], 1, 'ZaYO7nWVzCE.mp3'],
    ['beautiful tomorrow (Flower ver.)', [7], 3, 'OXVgMV3DdjY.mp3'],
    ['beautiful tomorrow (Bird ver.)', [7], 3, 'R4IF4YFTWas.mp3'],
    ['beautiful tomorrow (Wind ver.)', [7], 3, 'Brwcqn66dM4.mp3'],
    ['beautiful tomorrow (Moon ver.)', [7], 3, 'uGwuZCVAJbo.mp3'],
    ['beautiful tomorrow (Instrumental)', [7], 2, 'bp8vBhI6wT4.mp3'],
    ['私たちはまだその春を知らない', [7], 1, 'MycoRNcb6eM.mp3'],
    ['私たちはまだその春を知らない (Instrumental)', [7], 2, '65TZidvLC-Y.mp3'],
    ['Colorful', [8, 14], 1, 'g26XYhPd6C0.mp3'],
    ['Colorful (Flower ver.)', [8], 3, 'ZwokU805lQo.mp3'],
    ['Colorful (Bird ver.)', [8], 3, 'E4gPEFVguSQ.mp3'],
    ['Colorful (Wind ver.)', [8], 3, 'ezlOIGrmaGg.mp3'],
    ['Colorful (Moon ver.)', [8], 3, '3JW9cHAoEM.mp3'],
    ['Colorful (Instrumental)', [8], 2, 'Vo_5VVcE0F0.mp3'],
    ['カレイドスコープ', [8, 14], 1, 'XiiisM5bT4s.mp3'],
    ['カレイドスコープ (Instrumental)', [8], 2, 'hUJyOqf9Wuc.mp3'],
    ['Reach For The World!', [9], 1, 'tpnj5HR1nxQ.mp3'],
    ['Reach For The World! (Instrumental)', [9], 2, 'Czotm071qoI.mp3'],
    ['Determination-声の架け橋-', [9], 1, 'IYKO2q1dfxo.mp3'],
    ['Determination-声の架け橋- (Instrumental)', [9], 2, '0KIouB_96Cs.mp3'],
    ['NAZO-NAZE Jumping!', [10], 1, 'TyhAbFGsW1A.mp3'],
    ['NAZO-NAZE Jumping! (Instrumental)', [10], 2, 'RoPtu579cHs.mp3'],
    ['ぐっばいおぶじぇくしょん', [10], 1, 'bEXD8hAHiDE.mp3'],
    ['ぐっばいおぶじぇくしょん(Instrumental)', [10], 2, 'RNpHB5EFM8A.mp3'],
    ['Red or Blue？', [11], 1, 'xeRGBf6bHYo.mp3'],
    ['Red or Blue？ (Instrumental)', [11], 2, 'zqU8cM_aRes.mp3'],
    ['Field of Flowers', [11], 1, 'pcCV1jjMwr4.mp3'],
    ['Field of Flowers (Instrumental)', [11], 2, '2qQAIpOnH0M.mp3'],
    ['Override!', [12], 1, 'gORnlx9Ad3c.mp3'],
    ['Override! (Instrumental)', [12], 2, 'Q2KJEZk0cFE.mp3'],
    ['ハミングバード', [12], 1, 'vlv91TLsTHg.mp3'],
    ['ハミングバード(Instrumental)', [12], 2, 'wO6QfAFqMY8.mp3'],
    ['最高の魔法', [13, 14], 1, 'enSvModJ38k.mp3'],
    ['最高の魔法 (Flower ver.)', [13], 3, 'NeB2e2UkrLI.mp3'],
    ['最高の魔法 (Bird ver.)', [13], 3, 'zOwJ4ZDcQr0.mp3'],
    ['最高の魔法 (Wind ver.)', [13], 3, 'ntXnP-r8yWo.mp3'],
    ['最高の魔法 (Moon ver.)', [13], 3, 'fKJ5LkH0JZ8.mp3'],
    ['最高の魔法 (Instrumental)', [13], 2, 'gMeNKtegHVo.mp3'],
    ['白い沿線', [13], 1, 'R-xZpKD0xZs.mp3'],
    ['白い沿線 (Instrumental)', [13], 2, 'Al359qWstN4.mp3'],
    ['CUTE♡CUTE♡CUTE♡', [14], 1, 'lz2fSRWXqk.mp3'],
    ['CUTE♡CUTE♡CUTE♡ (Flower ver.)', [11], 3, '5ejczSIUkKE.mp3'],
    ['CUTE♡CUTE♡CUTE♡ (Bird ver.)', [12], 3, 'uyLB-iQ7ct8.mp3'],
    ['CUTE♡CUTE♡CUTE♡ (Wind ver.)', [10], 3, 'Mg5CF2mtpg0.mp3'],
    ['CUTE♡CUTE♡CUTE♡ (Moon ver.)', [9], 3, 'W25a-yf02vA.mp3'],
    ['our song', [14], 1, 'DyDA7QiIIio.mp3'],
    ['our song (Flower ver.)', [3], 3, '1hk9aikSTH4.mp3'],
    ['our song (Bird ver.)', [4], 3, 'hxw0_GyEKGU.mp3'],
    ['our song (Wind ver.)', [5], 3, 'Z_yt_xFErlk.mp3'],
    ['our song (Moon ver.)', [6], 3, '4Naf-YLFaZo.mp3'],
    ['ミライキャンバス', [14], 1, 'DCfvQyYil6Q.mp3'],
    ['Radio is a Friend!', [14], 1, 'bRu7zZSTooM.mp3'],
    ['マイサスティナー', [14], 1, 'OspUN8GjoNQ.mp3'],
    ['雫の結晶', [14], 1, 'UO2u_YjFNE8.mp3'],
    ['キセキなSummer！', [0], 1, '209.mp3'],
    ['Land"e"scape', [0], 1, '210.mp3'],
]

songtype = [
    [1, 'Normal'], [2, 'Instrumental'], [3, 'Team']
]

jsondata = {'Songs':[], 'SongTypes':[]}

for song in songs:
    songdata = {'name':song[0], 'discos':[], 'songtype':song[2], 'file':song[3]}
    for disco in song[1]:
        songdata['discos'].append({'disco':disco})
    jsondata['Songs'].append(songdata)

for stype in songtype:
    jsondata['SongTypes'].append({'id':stype[0], 'typename':stype[1]})

with open('songList.json', 'w', encoding='utf-8') as outfile:
    json.dump(jsondata, outfile, indent=4, ensure_ascii=False)