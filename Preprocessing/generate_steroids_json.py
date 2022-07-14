import json
from data_keys import steroid_reports_players

players_mlb = {}
with open("./Data/mlb_players.json", 'r') as json_file:
    players_mlb:dict = json.load(json_file)

scandals_players = {}

names = list(steroid_reports_players.keys())

for pId in players_mlb.keys():
    player = players_mlb[pId]
    #print(player['Url'])
    if player['Full Name'] in names:
        scandals_players[pId] = player

with open("./Data/jsons/scandals_players.json", 'w') as target:
    json.dump(scandals_players, target, indent=4)