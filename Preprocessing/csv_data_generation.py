import csv
import json

headers_bio = ['Id', 'Name', 'Active','First year','Last year','Url','Country','Bat hand','Throw hand','Full Name','HoF','HoF type','HoF year','HoF comittee','Player type','retirement_age','total_seasons','career_teams','career_leagues','first_position','second_position','play_in_mayors','play_in_negro_league']
headers_bat = ['2B_bt','3B_bt','AB_bt','BA_bt','BB_bt','CS_bt','G_bt','HR_bt','H_bt','IBB_bt','OBP_bt','OPS+_bt','OPS_bt','PA_bt','RAA_bt','RAR_bt','RBI_bt','R_bt','Rbaser_bt','Rbat_bt','Rdp_bt','Rfield_bt','Rpos_bt','Rrep_bt','SB_bt','SF_bt','SH_bt','SLG_bt','SO_bt','TB_bt','WAA_bt','WAR_bt','dWAR_bt','oRAR_bt','oWAR_bt','A_fd','CG_fd','CS%_fd','CS_fd','Ch_fd','DP_fd','E_fd','Fld%_fd','GS_fd','G_fd','Inn_fd','PB_fd','PO_fd','RF/9_fd','RF/G_fd','SB_fd','WP_fd']
headers_pit = ['W_pt','L_pt','W-L%_pt','ERA_pt','G_pt','GS_pt','GF_pt','CG_pt','SHO_pt','SV_pt','IP_pt','H_pt','R_pt','ER_pt','HR_pt','BB_pt','IBB_pt','SO_pt','HBP_pt','BK_pt','WP_pt','BF_pt','ERA+_pt','FIP_pt','WHIP_pt','H9_pt','HR9_pt','BB9_pt','SO9_pt','SO/W_pt','RAA_pt','WAA_pt','WAR_pt','RAR_pt']


batter_file = open('./Data/Corpus_csv/batters_all_career.csv', 'w', newline='')
batters_writer = csv.DictWriter(batter_file, fieldnames=headers_bio+headers_bat)
batters_writer.writeheader()

pitcher_file = open('./Data/Corpus_csv/pitchers_all_career.csv', 'w', newline='') 
pitchers_writer = csv.DictWriter(pitcher_file, fieldnames=headers_bio+headers_pit)
pitchers_writer.writeheader()

pit_bat_file = open('./Data/Corpus_csv/pit_bat_all_career.csv', 'w', newline='')
pit_bat_writer = csv.DictWriter(pit_bat_file, fieldnames=headers_bio+headers_pit+headers_bat)
pit_bat_writer.writeheader()

mlb_player_path = "./Data/mlb_players.json"
with open(mlb_player_path, 'r') as js_file:
    players_dict = json.load(js_file)

for id in players_dict.keys():
    player = players_dict[id]
    row = {k:player[k] for k in player.keys() if not k in ['batter_stats', 'field_stats', 'pitcher_stats', 'Positions']}
    player_type = player["Player type"] 
    if player_type != 2:
        p_stats = player["pitcher_stats"]
        for k in p_stats.keys():
          if k+"_bt" in headers_pit:
               row[k+'_bt'] = p_stats[k]["summary"]
    if player_type != 1:
        b_stats = player['batter_stats']
        f_stats = player['field_stats']
        for k in b_stats.keys():
          if k+"_bt" in headers_bat:
               row[k+'_bt'] = b_stats[k]["summary"]
        for k in f_stats.keys():
            if k+"_fd" in headers_bat:
               row[k+'_fd'] = f_stats[k]["summary"]
    if player_type == 1:
        pitchers_writer.writerow(row)
    elif player_type == 2:
        batters_writer.writerow(row)
    else:
        pit_bat_writer.writerow(row)


batter_file.close()
pitcher_file.close()
pit_bat_file.close()