from os import walk
import json
import re
from fielder_stats_calc import *
from data_keys import negro_leagues, leagues_mayors

numerical_stat_patron = re.compile('^-?(0|[1-9]\d*)?(\.\d+)?(?<=\d)$')

pos = {'Pitcher':"P",
    'Outfielder':"OF", 
    'Centerfielder':"CF", 
    'Leftfielder':"LF", 
    'Rightfielder':"RF",
    'Infielder':"IF",
    'First Baseman':"1B", 
    'Third Baseman':"3B",
    'Catcher':"C",
    'Second Baseman':"2B",
    'Shortstop':"SS",
    'Pinch Hitter':"PH",
    'Designated Hitter':"DH",
    'Pinch Runner':"PR"}

selected_bat_value_stats = {"Rbat","Rbaser","Rdp","Rfield","Rpos","RAA","WAA","Rrep","RAR","WAR","oWAR","dWAR","oRAR"}

selected_pit_value_stats = {"RAA","WAA","WAR","RAR"}

mlb_player = {}

print("Working...")
with open('./Data/mlb_players.json', 'w') as file:
    for dirpath, dirnames, filenames in walk("./Data/players"):
        for js in filenames:
            if js.endswith(".json"):
                js_path = dirpath+"/"+js
                with open(js_path, 'r') as js_file:  
                    player_dict = json.load(js_file)
                    c = player_dict["Country"]
                    if c == '':
                        player_dict["Country"] = c = "desconocido"
                    player_id = player_dict["Id"]
                    b_stats = {}
                    p_stats = {}
                    f_stats = {}
                    player_teams = []
                    retirement_age = -1
                    player_leagues = []
                    play_in_mayors = 0   #0 no, 1 si
                    play_in_negro_league = 0  #0 no, 1 si
                    total_years = -1
                    summary_position = ""
                    games_as_pitcher = 0
                    games_as_batter = 0

                    if len(player_dict["batter_stats"])>0: 
                        b_stats = {"Age":{},"Lg":{},"G":{},"PA":{},"AB":{},"R":{},"H":{},"2B":{},"3B":{},"HR":{},
                                    "RBI":{},"SB":{},"CS":{},"BB":{}, "SO":{}, "BA":{},"OBP":{},"SLG":{},"OPS":{},"OPS+":{},"TB":{},
                                    "SH":{},"SF":{},"IBB":{},"Rbat":{},"Rbaser":{},"Rdp":{},"Rfield":{},"Rpos":{},"RAA":{},"WAA":{},
                                    "Rrep":{},"RAR":{},"WAR":{},"oWAR":{},"dWAR":{},"oRAR":{}}
                        selected_stats = b_stats.keys()                     
                        years_bat_standard = player_dict["batter_stats"]["standard_stats"]['by_years']
                        summary_bat_standard = player_dict["batter_stats"]["standard_stats"]['summary']
                        for year_stats in years_bat_standard:
                            _y, _age = year_stats["Year"], year_stats["Age"]
                            _tm, _lg = year_stats["Tm"], year_stats["Lg"]
                            if not _tm in player_teams and _tm != "":
                                player_teams.append(_tm)
                            if not _lg in player_leagues and _lg != "":
                                player_leagues.append(_lg)
                            if isinstance(_age, float):
                                retirement_age = max(int(_age), retirement_age)
                            else: 
                                year_stats["Age"] = "desconocido"
                            for stat in year_stats.keys():
                                if stat in selected_stats:
                                    if isinstance(year_stats[stat], str):
                                        if numerical_stat_patron.search(year_stats[stat])!=None:
                                            b_stats[stat][_y] = float(year_stats[stat])
                                        else:
                                            b_stats[stat][_y] = year_stats[stat]
                                    else:
                                        b_stats[stat][_y] = year_stats[stat]
                        for stat in summary_bat_standard.keys():
                            if stat == "Year":
                                total_years = max(summary_bat_standard[stat],total_years)
                            elif stat in selected_stats:
                                    if isinstance(summary_bat_standard[stat], str):
                                        if numerical_stat_patron.search(summary_bat_standard[stat])!=None:
                                            b_stats[stat]['summary'] = float(summary_bat_standard[stat])
                                        else:
                                            b_stats[stat]['summary'] = summary_bat_standard[stat]
                                    else:
                                        b_stats[stat]["summary"] = summary_bat_standard[stat]
                        
                        years_bat_value = player_dict["batter_stats"]["value_stats"]['by_years']
                        summary_bat_value = player_dict["batter_stats"]["value_stats"]['summary']
                        for year_stats in years_bat_value:
                            _y = year_stats["Year"]
                            for stat in year_stats.keys():
                                if stat in selected_bat_value_stats:
                                    if b_stats[stat].get(_y) == None:
                                        b_stats[stat][_y] = 0
                                    if isinstance(year_stats[stat], str):
                                        if numerical_stat_patron.search(year_stats[stat])!=None:
                                            b_stats[stat][_y] += float(year_stats[stat])
                                        else:
                                            b_stats[stat][_y] += 0
                                    else:
                                        b_stats[stat][_y] += float(year_stats[stat])
                        
                        for stat in summary_bat_value.keys():
                            if stat in selected_bat_value_stats:
                                if isinstance(summary_bat_value[stat], str):
                                    if numerical_stat_patron.search(summary_bat_value[stat])!=None:
                                        b_stats[stat]['summary'] = float(summary_bat_value[stat])
                                    else:
                                        b_stats[stat]['summary'] = summary_bat_value[stat]
                                else:
                                    b_stats[stat]["summary"] = summary_bat_value[stat]
                        player_dict["batter_stats"] = b_stats

                    if len(player_dict["pitcher_stats"])>0:    
                        p_stats = {"Age":{},"Lg":{},"W":{},"L":{},"W-L%":{},"ERA":{},"G":{},"GS":{},"GF":{},
                        "CG":{},"SHO":{},"SV":{},"IP":{},"H":{},"R":{},"ER":{},"HR":{},"BB":{},"IBB":{},"SO":{},
                        "HBP":{},"BK":{},"WP":{},"BF":{},"ERA+":{},"FIP":{},"WHIP":{},"H9":{},"HR9":{},"BB9":{},
                        "SO9":{},"SO/W":{},"RAA":{},"WAA":{},"WAR":{},"RAR":{}}
                        selected_stats = p_stats.keys()                     
                        years_pit_standard = player_dict["pitcher_stats"]["standard_stats"]['by_years']
                        summary_pit_standard = player_dict["pitcher_stats"]["standard_stats"]['summary']
                        for year_stats in years_pit_standard:
                            _y, _age = year_stats["Year"], year_stats["Age"]
                            _tm, _lg = year_stats["Tm"], year_stats["Lg"]
                            if not _tm in player_teams and _tm != "":
                                player_teams.append(_tm)
                            if not _lg in player_leagues and _lg != "":
                                player_leagues.append(_lg)
                            if isinstance(_age, float):
                                retirement_age = max(int(_age), retirement_age)
                            else: 
                                year_stats["Age"] = "desconocido"
                            for stat in year_stats.keys():
                                if stat in selected_stats:
                                    if isinstance(year_stats[stat], str):
                                        if numerical_stat_patron.search(year_stats[stat])!=None:
                                            p_stats[stat][_y] = float(year_stats[stat])
                                        else:
                                            p_stats[stat][_y] = year_stats[stat]
                                    else:
                                        p_stats[stat][_y] = year_stats[stat]
                        for stat in summary_pit_standard.keys():
                            if stat == "Year":
                                total_years = max(summary_pit_standard[stat],total_years)
                            elif stat in selected_stats:
                                    if isinstance(summary_pit_standard[stat], str):
                                        if numerical_stat_patron.search(summary_pit_standard[stat])!=None:
                                            p_stats[stat]['summary'] = float(summary_pit_standard[stat])
                                        else:
                                            p_stats[stat]['summary'] = summary_pit_standard[stat]
                                    else:
                                        p_stats[stat]["summary"] = summary_pit_standard[stat]                        
                        years_pit_value = player_dict["pitcher_stats"]["value_stats"]['by_years']
                        summary_pit_value = player_dict["pitcher_stats"]["value_stats"]['summary']
                        for year_stats in years_pit_value:
                            _y = year_stats["Year"]
                            for stat in year_stats.keys():
                                if stat in selected_pit_value_stats:
                                    if p_stats[stat].get(_y) == None:
                                        p_stats[stat][_y] = 0
                                    if isinstance(year_stats[stat], str):
                                        if numerical_stat_patron.search(year_stats[stat])!=None:
                                            p_stats[stat][_y] += float(year_stats[stat])
                                        else:
                                            p_stats[stat][_y] += 0
                                    else:
                                        p_stats[stat][_y] += float(year_stats[stat])                       
                        for stat in summary_pit_value.keys():
                            if stat in selected_pit_value_stats:
                                if isinstance(summary_pit_value[stat], str):
                                    if numerical_stat_patron.search(summary_pit_value[stat])!=None:
                                        p_stats[stat]['summary'] = float(summary_pit_value[stat])
                                    else:
                                        p_stats[stat]['summary'] = summary_pit_value[stat]
                                else:
                                    p_stats[stat]["summary"] = summary_pit_value[stat]
                        player_dict["pitcher_stats"] = p_stats

                    if len(player_dict["field_stats"])>0:    
                        f_stats = {"Age":{},"G":{},"GS":{},"CG":{},"Inn":{},"PO":{},"A":{},"E":{},"DP":{},
                                    "PB":{},"WP":{},"SB":{},"CS":{}}
                        selected_stats = f_stats.keys()                     
                        years_field_standard = player_dict["field_stats"]['by_years']
                        summary_position = player_dict["field_stats"]['summary']['Pos']

                        data_years = []
                        for year_stats in years_field_standard:
                            _y = year_stats["Year"]
                            if not _y in data_years:
                                data_years.append(_y)
                            for stat in year_stats.keys():
                                if stat in selected_stats:
                                    if f_stats[stat].get(_y) == None:
                                        f_stats[stat][_y] = 0.0
                                    if stat == "Age":
                                        f_stats["Age"][_y] = year_stats["Age"]
                                    elif stat == "Inn":
                                        new_inn = float(year_stats[stat]) if numerical_stat_patron.search(year_stats[stat])!=None else 0.0
                                        f_stats[stat][_y] = inning_sum(new_inn,f_stats[stat][_y])   
                                    elif isinstance(year_stats[stat], str):
                                        if numerical_stat_patron.search(year_stats[stat])!=None:
                                            f_stats[stat][_y] += float(year_stats[stat])
                                        else:
                                            f_stats[stat][_y] += 0
                                    else:
                                        f_stats[stat][_y] += float(year_stats[stat])
                        #make standard stats summary
                        for stat in f_stats.keys():
                            if len(f_stats[stat]) > 0 and stat not in ["Lg", "Age", "Year"]:
                                if stat == "Inn":
                                    inn_ac = 0.0
                                    for inn in f_stats[stat].values():
                                        inn_ac = inning_sum(inn, inn_ac)
                                    f_stats[stat]["summary"] = inn_ac
                                else:
                                    f_stats[stat]["summary"] = sum(f_stats[stat].values())
                        # add advanced stats yearly
                        inn, g, assists, err, putouts = f_stats["Inn"], f_stats["G"], f_stats["A"], f_stats["E"], f_stats["PO"]
                        f_stats["Ch"], f_stats["Fld%"], f_stats["RF/9"], f_stats["RF/G"] = {},{},{},{}
                        for year in data_years:
                            f_stats["Ch"][year] = defensive_chaces(putout=putouts[year],assists=assists[year], errors=err[year])
                            f_stats["Fld%"][year] = fielding_percentage(putout=putouts[year],assists=assists[year], errors=err[year])
                            f_stats["RF/9"][year] = range_factor_per_9_inng(putout=putouts[year],assists=assists[year], inn=inn[year])
                            f_stats["RF/G"][year] = range_factor_per_game(putout=putouts[year],assists=assists[year], gplayed=g[year])
                        # add advanced stats summary
                        f_stats["Ch"]["summary"] = defensive_chaces(putout=putouts["summary"],assists=assists["summary"], errors=err["summary"])
                        f_stats["Fld%"]["summary"] = fielding_percentage(putout=putouts["summary"],assists=assists["summary"], errors=err["summary"])
                        f_stats["RF/9"]["summary"] = range_factor_per_9_inng(putout=putouts["summary"],assists=assists["summary"], inn=inn["summary"])
                        f_stats["RF/G"]["summary"] = range_factor_per_game(putout=putouts["summary"],assists=assists["summary"], gplayed=g["summary"])

                        if "Catcher" in player_dict["Positions"]:
                            sb, cs = f_stats['SB'], f_stats['CS']
                            if len(sb) > 0 and len(cs) > 0:
                                f_stats["CS%"] = {}
                                for year in data_years:
                                    f_stats["CS%"][year] = caught_stealing_percentage(stolen_bases=sb[year], caught_stealing=cs[year])
                                f_stats["CS%"]["summary"] = caught_stealing_percentage(stolen_bases=sb["summary"], caught_stealing=cs["summary"])

                        player_dict["field_stats"] = f_stats

                    player_dict["retirement_age"] = retirement_age if retirement_age != -1 else "desconocido"
                    player_dict["total_seasons"] = total_years
                    if "MLB" in player_leagues:
                        player_leagues.remove("MLB")
                        if not "AL" in player_leagues:
                            player_leagues.append("AL")
                        if not "NL" in player_leagues:
                            player_leagues.append("NL")
                    if "TOT" in player_teams:
                        player_teams.remove("TOT")
                    player_dict["career_teams"] = player_teams
                    player_dict['career_leagues'] = player_leagues
                    for lg in player_leagues:
                        if lg in negro_leagues:
                            play_in_negro_league = 1
                        elif lg in leagues_mayors:
                            play_in_mayors = 1
                    player_dict['play_in_mayors'] = play_in_mayors
                    player_dict['play_in_negro_league'] = play_in_negro_league
                    player_dict['two_way_player'] = 0
                    ab_positions = []
                    for p in player_dict["Positions"]:
                        ab_positions.append(pos[p])
                    first_postition = "-"
                    second_position = "-"
                    if player_dict['Player type'] == 1:
                        first_postition = "P"
                    elif player_dict['Player type'] == 2:
                        if len(ab_positions)==1:
                            first_postition = ab_positions[0]
                        elif len(ab_positions) > 1:
                            first_postition = summary_position
                            for p in ab_positions:
                                if p != first_postition:
                                    second_position = p
                                    break
                    else:
                        games_as_pitcher = p_stats["G"]["summary"]
                        games_as_batter = b_stats["G"]["summary"]
                        if games_as_batter > games_as_pitcher:
                            player_dict['Player type'] = 2
                            if summary_position != "P":
                                first_postition = summary_position
                                second_position = "P"
                            else:
                                second_postition = summary_position
                                for p in ab_positions:
                                    if p != "P":
                                        first_postition = p
                        else:
                            player_dict['Player type'] = 1
                            if summary_position == "P":
                                first_postition = summary_position
                                for p in ab_positions:
                                    if p != "P":
                                        second_postition = p
                            else:
                                first_postition == "P"
                                second_postition = summary_position
                        player_dict['two_way_player'] = 1 if games_as_batter > 159 and games_as_pitcher>159 else 0

                    player_dict["Positions"] = ab_positions
                    player_dict['first_position'] = first_postition
                    player_dict['second_position'] = second_position
                    mlb_player[player_id] = player_dict

    json.dump(mlb_player, file, indent=4)
print("Work finish!!!")