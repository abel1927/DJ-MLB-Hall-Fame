import csv
import json
from data_keys import headers_bio, headers_pit, headers_bat

batter_file = open('./Data/Corpus_csv/batters_all_career.csv', 'w', newline='')
batters_writer = csv.DictWriter(batter_file, fieldnames=headers_bio+headers_bat)
batters_writer.writeheader()

pitcher_file = open('./Data/Corpus_csv/pitchers_all_career.csv', 'w', newline='') 
pitchers_writer = csv.DictWriter(pitcher_file, fieldnames=headers_bio+headers_pit)
pitchers_writer.writeheader()

mlb_player_path = "./Data/mlb_players.json"
with open(mlb_player_path, 'r') as js_file:
    players_dict = json.load(js_file)

for id in players_dict.keys():
    player = players_dict[id]
    row = {k:player[k] for k in player.keys() if not k in ['batter_stats', 'field_stats', 'pitcher_stats', 'Positions']}
    player_type = player["Player type"] 
    if player_type == 1:
        p_stats = player["pitcher_stats"]
        for k in p_stats.keys():
          if k+"_bt" in headers_pit:
               row[k+'_bt'] = p_stats[k]["summary"]
    if player_type == 2:
        b_stats = player['batter_stats']
        f_stats = player['field_stats']
        for k in b_stats.keys():
          if k+"_bt" in headers_bat:
               row[k+'_bt'] = b_stats[k]["summary"]
        for k in f_stats.keys():
            if k+"_fd" in headers_bat:
                if f_stats[k].get('summary')!= None:
                    row[k+'_fd'] = f_stats[k]["summary"]

    if player_type == 1:
        pitchers_writer.writerow(row)
    elif player_type == 2:
        batters_writer.writerow(row)


batter_file.close()
pitcher_file.close()