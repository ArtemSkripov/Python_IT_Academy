# Задание 4
# У вас есть файл matches.json с результатами прошедших игр.
# Внутри каждого матча есть список игроков и их показатели
# (убийства, смерти, очки).
# Исходные данные (matches.json):
# [
# {
# "match_id": "m_101",
# "map": "Dust2",
# "players": [
# {"nickname": "Shadow", "kills": 22, "deaths": 14},
# {"nickname": "Viper", "kills": 15, "deaths": 18}
# ]
# },
# {
# "match_id": "m_102",
# "map": "Mirage",
# "players": [
# {"nickname": "Shadow", "kills": 18, "deaths": 18},
# {"nickname": "Ghost", "kills": 25, "deaths": 10}
# ]
# }
# ]
# 1. Прочитать файл matches.json.
# 2. Посчитать общий K/D (отношение убийств к смертям)
# для каждого игрока по всем матчам, округлив до 2 знаков
# после запятой.
# 3. Найти лучшего игрока (с самым высоким K/D).
# 4. Сохранить результат в файл leaderboard.json,
# отсортировав игроков от лучшего к худшему.

import json

with open('matches.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    players_list={}
    for match in data:
        for player in match['players']:
            nick = player['nickname']
            if nick not in players_list:
                players_list[nick] = {'kills':0,'deaths':0}
            players_list[nick]['kills'] += player['kills']
            players_list[nick]['deaths'] += player['deaths']
            
    leaderbord = []
    for nick in players_list:
        kills = players_list[nick]['kills']
        deaths = players_list[nick]['deaths']
        if deaths > 0:
            kd = round(kills / deaths, 2)
        else:
            kd = kills
        player_info = {'nickname': nick, 'kd': kd}
        leaderbord.append(player_info)
    print(players_list)
    print(leaderbord)
    
    for i in range(len(leaderbord)):
        for j in range(len(leaderbord) - 1):
   
            if leaderbord[j]['kd'] < leaderbord[j + 1]['kd']:
                temp = leaderbord[j]
                leaderbord[j] = leaderbord[j + 1]
                leaderbord[j + 1] = temp


best_player = leaderbord[0]
print('Лучший игрок:', best_player['nickname'], 'с K/D:', best_player['kd'])


with open('leaderboard.json', 'w', encoding='utf-8') as out_file:
  json.dump(leaderbord, out_file, indent=4)