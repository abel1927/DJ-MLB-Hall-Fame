import csv
import json
from data_keys import headers_bio
from data_keys import bat_basic_stats, bat_calc_stats
from data_keys import field_basic_stats, field_calc_stats
from data_keys import pit_basic_stats, pit_calc_stats
from stats_calc.batter_stats_calc import *
from stats_calc.fielder_stats_calc import *
from stats_calc.pitcher_stats_calc import *
import numpy as np

def x_season_bat_stats_summary(bat_stats,x=10):
    compute_stat = {}
    x_season_age = -1
    for stat in bat_stats.keys():
        if not stat+'_bt' in bat_basic_stats:
            if stat == "Age":
                x_season_age = [a for a in bat_stats[stat].values()][x-1]
            continue
        compute_stat[stat+'_bt'] =  [x for x in bat_stats[stat].values()][:x]
    for stat in compute_stat.keys():
        yearly = compute_stat[stat]
        summary = 0
        for v in yearly:
            summary = summary + v if isinstance(v, float) else summary
        compute_stat[stat] = summary
    compute_stat['BA_bt'] = batting_average(compute_stat["H_bt"], compute_stat["AB_bt"])
    compute_stat['OBP_bt'] = batting_obp(compute_stat['H_bt'], compute_stat['BB_bt'], compute_stat["HBP_bt"], 
                            compute_stat["AB_bt"], compute_stat["SF_bt"])
    compute_stat["SLG_bt"] = slugger(compute_stat['H_bt'], compute_stat['2B_bt'], compute_stat['HR_bt'], compute_stat['HR_bt'], compute_stat['AB_bt'])
    compute_stat['TB_bt'] = total_bases(compute_stat['H_bt'], compute_stat['2B_bt'], compute_stat['3B_bt'], compute_stat["HR_bt"])
    compute_stat['OPS_bt'] = batting_ops(compute_stat['OBP_bt'],compute_stat["SLG_bt"])
    return compute_stat, x_season_age

def x_season_field_stats_summary(field_stats,x=10):
    compute_stat = {}
    for stat in field_stats.keys():
        if not stat+'_fd' in field_basic_stats:
            continue
        compute_stat[stat+'_fd'] =  [x for x in field_stats[stat].values()][:x]
    for stat in compute_stat.keys():
        yearly = compute_stat[stat]
        summary = 0
        for v in yearly:
            if stat == 'Inn_fd':
                summary = inning_sum(summary, v) if isinstance(v, float) else summary
            else:
                summary = summary + v if isinstance(v, float) else summary
        compute_stat[stat] = summary
    compute_stat["Fld%_fd"] = fielding_percentage(compute_stat["PO_fd"], compute_stat["A_fd"], compute_stat["E_fd"])
    compute_stat["Ch_fd"] = defensive_chaces(compute_stat["PO_fd"], compute_stat['A_fd'], compute_stat['E_fd'])
    return compute_stat

def x_season_pit_stats_summary(pit_stats,x=10):
    compute_stat = {}
    x_season_age = -1
    for stat in pit_stats.keys():
        if not stat+'_pt' in pit_basic_stats:
            if stat == "Age":
                l = min(len(pit_stats[stat].values()), x)
                x_season_age = [a for a in pit_stats[stat].values()][l-1]
            continue
        compute_stat[stat+'_pt'] = [x for x in pit_stats[stat].values()][:x]
    for stat in compute_stat.keys():
        yearly = compute_stat[stat]
        summary = 0
        for v in yearly:
            if stat == 'IP_fd':
                summary = inning_sum(summary, v) if isinstance(v, float) else summary
            else:
                summary = summary + v if isinstance(v, float) else summary
        compute_stat[stat] = summary
    compute_stat['W-L%_pt'] = win_lose_percentage(compute_stat['W_pt'],compute_stat['L_pt'])
    compute_stat['ERA_pt'] = era(compute_stat['R_pt'], compute_stat['IP_pt'])
    compute_stat['WHIP_pt'] = whip(compute_stat['BB_pt'], compute_stat['H_pt'], compute_stat['IP_pt'])
    compute_stat['H9_pt'] = h9(compute_stat['H_pt'], compute_stat['IP_pt'])
    compute_stat['HR9_pt'] = h9(compute_stat['HR_pt'], compute_stat['IP_pt'])
    compute_stat['BB9_pt'] = h9(compute_stat['BB_pt'], compute_stat['IP_pt'])
    compute_stat['SO9_pt'] = h9(compute_stat['SO_pt'], compute_stat['IP_pt'])
    compute_stat['SO/W_pt'] = h9(compute_stat['SO_pt'], compute_stat['W_pt'])
    compute_stat['FIP_pt'] = fip(compute_stat['HR_pt'], compute_stat['BB_pt'], compute_stat['HBP_pt'], 
                                compute_stat['SO_pt'], compute_stat['IP_pt'])
    return compute_stat, x_season_age

print("Started...")

batter_file = open('./Data/Corpus_csv/batters_ten_season.csv', 'w', newline='')
batters_writer = csv.DictWriter(batter_file, fieldnames=headers_bio+["ten_season_age"]+bat_basic_stats+bat_calc_stats+field_basic_stats+field_calc_stats)
batters_writer.writeheader()

pitcher_file = open('./Data/Corpus_csv/pitchers_ten_season.csv', 'w', newline='') 
pitchers_writer = csv.DictWriter(pitcher_file, fieldnames=headers_bio+["ten_season_age"]+pit_basic_stats+pit_calc_stats)
pitchers_writer.writeheader()

mlb_player_path = "./Data/mlb_players.json"
with open(mlb_player_path, 'r') as js_file:
    players_dict = json.load(js_file)

for id in players_dict.keys():
    player = players_dict[id]
    if player["total_seasons"] < 10:
        continue
    row = {k:player[k] for k in player.keys() if not k in ['batter_stats', 'field_stats', 'pitcher_stats', 'Positions']}
    player_type = player["Player type"] 
    if player_type == 1:
        stats, age = x_season_pit_stats_summary(player["pitcher_stats"])
        row["ten_season_age"] = age
        row.update(stats)
    if player_type == 2:
        stats, age = x_season_bat_stats_summary(player['batter_stats'])
        row['ten_season_age'] = age
        row.update(stats)
        row.update(x_season_field_stats_summary(player['field_stats']))

    if player_type == 1:
        pitchers_writer.writerow(row)
    elif player_type == 2:
        batters_writer.writerow(row)


batter_file.close()
pitcher_file.close()

print("Finish!!")