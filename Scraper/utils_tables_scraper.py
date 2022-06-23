from bs4 import BeautifulSoup, Comment
import re

#url = "https://www.baseball-reference.com/players/c/canoro01.shtml"
#url = "https://www.baseball-reference.com/players/p/posadjo01.shtml"
#url = 'https://www.baseball-reference.com/players/f/florody01.shtml'

#res = requests.get(url)
#soup = BeautifulSoup(res.text, 'html.parser')

#b_std_heads = {'year_ID': 'Year', 'age': 'Age', 'team_ID': 'Tm', 'lg_ID': 'Lg', 'G': 'G', 'PA': 'PA', 
#'AB': 'AB', 'R': 'R', 'H': 'H', '2B': '2B', '3B': '3B', 'HR': 'HR', 'RBI': 'RBI', 'SB': 'SB', 'CS': 'CS', 
#'BB': 'BB', 'SO': 'SO', 'batting_avg': 'BA', 'onbase_perc': 'OBP', 'slugging_perc': 'SLG', 'onbase_plus_slugging': 'OPS', 
#'onbase_plus_slugging_plus': 'OPS+', 'TB': 'TB', 'GIDP': 'GDP', 'HBP': 'HBP', 'SH': 'SH', 'SF': 'SF', 
#'IBB': 'IBB'}#, 'pos_season': 'Pos', 'award_summary': 'Awards'}

#b_value_heads = {'year_ID': 'Year', 'age': 'Age', 'team_ID': 'Tm', 'lg_ID': 'Lg', 'G': 'G', 'PA': 'PA', 
#'runs_bat': 'Rbat', 'runs_br': 'Rbaser', 'runs_dp': 'Rdp', 'runs_fielding': 'Rfield', 'runs_pos': 'Rpos',
#'runs_above_avg_bat': 'RAA', 'WAA': 'WAA', 'runs_replacement': 'Rrep', 'runs_above_rep': 'RAR', 'WAR': 'WAR',
# 'waa_win_perc': 'waaWL%', 'waa_win_perc_162': '162WL%', 'WAR_off': 'oWAR', 'WAR_def': 'dWAR', 
# 'runs_above_rep_off': 'oRAR'}#, 'Salary': 'Salary', 'pos_season': 'Pos', 'award_summary': 'Awards'}

#head_std = ['Year','Age','Tm','Lg','G','PA','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO',
#'BA','OBP','SLG','OPS','OPS+','TB','GDP','HBP','SH','SF','IBB']#,'Pos','Awards']

#head_value = ['Year','Age','Tm','Lg','G','PA','Rbat','Rbaser','Rdp','Rfield','Rpos','RAA','WAA','Rrep',
#'RAR','WAR','waaWL%','162WL%','oWAR','dWAR','oRAR','Salary','Pos','Awards']



#e = ['Year','age', 'team_ID', 'lg_ID', 'G', 'PA', 'runs_bat', 'runs_br', 'runs_dp', 'runs_fielding', 'runs_pos', 'runs_above_avg_bat', 'WAA', 'runs_replacement', 'runs_above_rep', 'WAR', 'waa_win_perc', 'waa_win_perc_162', 'WAR_off', 'WAR_def', 'runs_above_rep_off', 'Salary', 'pos_season', 'award_summary']


#d = ['year_ID','age', 'team_ID', 'lg_ID', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 
#'SB', 'CS', 'BB', 'SO', 'batting_avg', 'onbase_perc', 'slugging_perc', 'onbase_plus_slugging', 
#'onbase_plus_slugging_plus', 'TB', 'GIDP', 'HBP', 'SH', 'SF', 'IBB']#, 'pos_season', 'award_summary']

def get_standard_batting_table(soup:BeautifulSoup):
    b_std_heads = {'year_ID': 'Year', 'age': 'Age', 'team_ID': 'Tm', 'lg_ID': 'Lg', 'G': 'G', 'PA': 'PA', 
    'AB': 'AB', 'R': 'R', 'H': 'H', '2B': '2B', '3B': '3B', 'HR': 'HR', 'RBI': 'RBI', 'SB': 'SB', 'CS': 'CS', 
    'BB': 'BB', 'SO': 'SO', 'batting_avg': 'BA', 'onbase_perc': 'OBP', 'slugging_perc': 'SLG', 'onbase_plus_slugging': 'OPS', 
    'onbase_plus_slugging_plus': 'OPS+', 'TB': 'TB', 'GIDP': 'GDP', 'HBP': 'HBP', 'SH': 'SH', 'SF': 'SF', 
    'IBB': 'IBB'}#, 'pos_season': 'Pos', 'award_summary': 'Awards'}
    std_table = []
    std_batting_table = soup.find('table', attrs={'id':'batting_standard'}).find('tbody')
    for row in std_batting_table.findAll('tr', attrs={'id': re.compile('batting_standard.(\d{4})')}):
        std = {}    
        y = row.find('th').text
        std['Year'] = int(y) if y.isnumeric() else y
        for col in row.findAll('td'):
            if b_std_heads.get(col['data-stat']) != None:
                std[b_std_heads[col['data-stat']]] = float(col.text) if col.text.isnumeric() else col.text
        std_table.append(std)
    
    std_batting_foot = soup.find('table', attrs={'id':'batting_standard'}).find('tfoot').find('tr')
    summary = {}
    summary['Year'] = int(re.search("\d+",std_batting_foot.find('th').text).group(0))
    for col in std_batting_foot.findAll('td'):
        if col['data-stat'] == "lg_ID":
            continue
        else:
            if b_std_heads.get(col['data-stat']) != None:
                summary[b_std_heads[col['data-stat']]] = float(col.text) if col.text.isnumeric() else col.text

    return std_table, summary


def get_value_batting_table(soup:BeautifulSoup):
    b_value_heads = {'year_ID': 'Year','G': 'G', 'PA': 'PA', 
    'runs_bat': 'Rbat', 'runs_br': 'Rbaser', 'runs_dp': 'Rdp', 'runs_fielding': 'Rfield', 'runs_pos': 'Rpos',
    'runs_above_avg_bat': 'RAA', 'WAA': 'WAA', 'runs_replacement': 'Rrep', 'runs_above_rep': 'RAR', 'WAR': 'WAR',
     'waa_win_perc': 'waaWL%', 'waa_win_perc_162': '162WL%', 'WAR_off': 'oWAR', 'WAR_def': 'dWAR', 
     'runs_above_rep_off': 'oRAR'}#, 'Salary': 'Salary', 'pos_season': 'Pos', 'award_summary': 'Awards'}
    value_table = []
    value_batting_table = soup.find('table', attrs={'id':'batting_value'}).find('tbody')
    for row in value_batting_table.findAll('tr', attrs={'id': re.compile('batting_value.(\d{4})')}):
        value = {}    
        y = row.find('th').text
        value['Year'] = int(y) if y.isnumeric() else y
        for col in row.findAll('td'):
            if b_value_heads.get(col['data-stat']) != None:
                value[b_value_heads[col['data-stat']]] = float(col.text) if col.text.isnumeric() else col.text
        value_table.append(value)
    
    value_batting_foot = soup.find('table', attrs={'id':'batting_value'}).find('tfoot').find('tr')
    summary = {}
    summary['Year'] = int(re.search("\d+",value_batting_foot.find('th').text).group(0))
    for col in value_batting_foot.findAll('td'):
        if col['data-stat'] == "lg_ID":
            continue
        else:
            if b_value_heads.get(col['data-stat']) != None:
                summary[b_value_heads[col['data-stat']]] = float(col.text) if col.text.isnumeric() else col.text

    return value_table, summary

#pit_head = ['Year', 'Age', 'Tm', 'Lg', 'W', 'L', 'W-L%', 'ERA', 'G', 'GS', 'GF', 'CG', 'SHO', 'SV', 'IP', 
#'H', 'R', 'ER', 'HR', 'BB', 'IBB', 'SO', 'HBP', 'BK', 'WP', 'BF', 'ERA+', 'FIP', 'WHIP', 'H9', 'HR9', 'BB9',
##'SO9', 'SO/W', 'Awards']

#pit_val = ['Year', 'Age', 'Tm', 'Lg', 'IP', 'G', 'GS', 'R', 'RA9', 'RA9opp', 'RA9def', 'RA9role', 'RA9extras',
#'PPFp', 'RA9avg', 'RAA', 'WAA', 'gmLI', 'WAAadj', 'WAR', 'RAR', 'waaWL%', '162WL%', 'Salary', 'Awards']

#x = ['year_ID', 'age', 'team_ID', 'lg_ID', 'W', 'L', 'win_loss_perc', 'earned_run_avg', 'G', 'GS', 'GF', 
#'CG', 'SHO', 'SV', 'IP', 'H', 'R', 'ER', 'HR', 'BB', 'IBB', 'SO', 'HBP', 'BK', 'WP', 'batters_faced', 
#'earned_run_avg_plus', 'fip', 'whip', 'hits_per_nine', 'home_runs_per_nine', 'bases_on_balls_per_nine', 
#'strikeouts_per_nine', 'strikeouts_per_base_on_balls', 'award_summary']

#p_std_heads = {'year_ID': 'Year', 'age': 'Age', 'team_ID': 'Tm', 'lg_ID': 'Lg', 'W': 'W', 'L': 'L', 
#'win_loss_perc': 'W-L%', 'earned_run_avg': 'ERA', 'G': 'G', 'GS': 'GS', 'GF': 'GF', 'CG': 'CG', 'SHO': 'SHO',
# 'SV': 'SV', 'IP': 'IP', 'H': 'H', 'R': 'R', 'ER': 'ER', 'HR': 'HR', 'BB': 'BB', 'IBB': 'IBB', 'SO': 'SO', 
# 'HBP': 'HBP', 'BK': 'BK', 'WP': 'WP', 'batters_faced': 'BF', 'earned_run_avg_plus': 'ERA+', 'fip': 'FIP', 
# 'whip': 'WHIP', 'hits_per_nine': 'H9', 'home_runs_per_nine': 'HR9', 'bases_on_balls_per_nine': 'BB9', 
# 'strikeouts_per_nine': 'SO9', 'strikeouts_per_base_on_balls': 'SO/W'}#, 'award_summary': 'Awards'}

#p_value_heads = {'year_ID': 'Year', 'age': 'Age', 'team_ID': 'Tm', 'lg_ID': 'Lg', 'IP': 'IP', 'G': 'G', 
#'GS': 'GS', 'R': 'R', 'runs_avg': 'RA9', 'opp_runs_avg': 'RA9opp', 'runs_avg_defense': 'RA9def', 
#'runs_avg_sprp': 'RA9role', 'runs_avg_extras': 'RA9extras', 'PPF_custom': 'PPFp', 
#'runs_avg_avg_pitcher': 'RA9avg', 'runs_above_avg_pitch': 'RAA', 'WAA': 'WAA', 
#'GR_leverage_index_avg': 'gmLI', 'WAA_adj': 'WAAadj', 'WAR_pitch': 'WAR', 'runs_above_rep_pitch': 'RAR', 
#'waa_win_perc': 'waaWL%', 'waa_win_perc_162': '162WL%'}#, 'Salary': 'Salary', 'award_summary': 'Awards'}

#f = ['year_ID','age', 'team_ID', 'lg_ID', 'IP', 'G', 'GS', 'R', 'runs_avg', 'opp_runs_avg', 
#'runs_avg_defense', 'runs_avg_sprp', 'runs_avg_extras', 'PPF_custom', 'runs_avg_avg_pitcher', 
#'runs_above_avg_pitch', 'WAA', 'GR_leverage_index_avg', 'WAA_adj', 'WAR_pitch', 'runs_above_rep_pitch', 
#'waa_win_perc', 'waa_win_perc_162', 'Salary', 'award_summary']

def get_standard_pitching_table(soup:BeautifulSoup):
    p_std_heads = {'year_ID': 'Year', 'age': 'Age', 'team_ID': 'Tm', 'lg_ID': 'Lg', 'W': 'W', 'L': 'L', 
    'win_loss_perc': 'W-L%', 'earned_run_avg': 'ERA', 'G': 'G', 'GS': 'GS', 'GF': 'GF', 'CG': 'CG', 'SHO': 'SHO',
     'SV': 'SV', 'IP': 'IP', 'H': 'H', 'R': 'R', 'ER': 'ER', 'HR': 'HR', 'BB': 'BB', 'IBB': 'IBB', 'SO': 'SO', 
     'HBP': 'HBP', 'BK': 'BK', 'WP': 'WP', 'batters_faced': 'BF', 'earned_run_avg_plus': 'ERA+', 'fip': 'FIP', 
     'whip': 'WHIP', 'hits_per_nine': 'H9', 'home_runs_per_nine': 'HR9', 'bases_on_balls_per_nine': 'BB9', 
     'strikeouts_per_nine': 'SO9', 'strikeouts_per_base_on_balls': 'SO/W'}#, 'award_summary': 'Awards'}
    std_table = []
    std_pitching_table = soup.find('table', attrs={'id':'pitching_standard'}).find('tbody')
    for row in std_pitching_table.findAll('tr', attrs={'id': re.compile('pitching_standard.(\d{4})')}):
        std = {}    
        y = row.find('th').text
        std['Year'] = int(y) if y.isnumeric() else y
        for col in row.findAll('td'):
            if p_std_heads.get(col['data-stat']) != None:
                std[p_std_heads[col['data-stat']]] = float(col.text) if col.text.isnumeric() else col.text
        std_table.append(std)
    
    std_pitching_foot = soup.find('table', attrs={'id':'pitching_standard'}).find('tfoot').find('tr')
    summary = {}
    summary['Year'] = int(re.search("\d+",std_pitching_foot.find('th').text).group(0))
    for col in std_pitching_foot.findAll('td'):
        if col['data-stat'] == "lg_ID":
            continue
        else:
            if p_std_heads.get(col['data-stat']) != None:
                summary[p_std_heads[col['data-stat']]] = float(col.text) if col.text.isnumeric() else col.text

    return std_table, summary


def get_value_pitching_table(soup:BeautifulSoup):
    p_value_heads = {'year_ID': 'Year', 'age': 'Age', 'team_ID': 'Tm', 'lg_ID': 'Lg', 'IP': 'IP', 'G': 'G', 
    'GS': 'GS', 'R': 'R', 'runs_avg': 'RA9', 'opp_runs_avg': 'RA9opp', 'runs_avg_defense': 'RA9def', 
    'runs_avg_sprp': 'RA9role', 'runs_avg_extras': 'RA9extras', 'PPF_custom': 'PPFp', 
    'runs_avg_avg_pitcher': 'RA9avg', 'runs_above_avg_pitch': 'RAA', 'WAA': 'WAA', 
    'GR_leverage_index_avg': 'gmLI', 'WAA_adj': 'WAAadj', 'WAR_pitch': 'WAR', 'runs_above_rep_pitch': 'RAR', 
    'waa_win_perc': 'waaWL%', 'waa_win_perc_162': '162WL%'}#, 'Salary': 'Salary', 'award_summary': 'Awards'}
    value_table = []
    value_pitching_table = soup.find('table', attrs={'id':'pitching_value'}).find('tbody')
    for row in value_pitching_table.findAll('tr', attrs={'id': re.compile('pitching_value.(\d{4})')}):
        value = {}    
        y = row.find('th').text
        value['Year'] = int(y) if y.isnumeric() else y
        for col in row.findAll('td'):
            if p_value_heads.get(col['data-stat']) != None:
                value[p_value_heads[col['data-stat']]] = float(col.text) if col.text.isnumeric() else col.text
        value_table.append(value)
    
    value_pitching_foot = soup.find('table', attrs={'id':'pitching_value'}).find('tfoot').find('tr')
    summary = {}
    summary['Year'] = int(re.search("\d+",value_pitching_foot.find('th').text).group(0))
    for col in value_pitching_foot.findAll('td'):
        if col['data-stat'] == "lg_ID":
            continue
        else:
            if p_value_heads.get(col['data-stat']) != None:
                summary[p_value_heads[col['data-stat']]] = float(col.text) if col.text.isnumeric() else col.text

    return value_table, summary




####Fielding

def get_standard_fielding_table(soup:BeautifulSoup):
    f_std_heads = {'year_ID': 'Year', 'age': 'Age', 'team_ID': 'Tm', 'pos': 'Pos', 'lg_ID': 'Lg', 'G': 'G', 
    'GS': 'GS', 'CG': 'CG', 'Inn_def': 'Inn', 'chances': 'Ch', 'PO': 'PO', 'A': 'A', 'E_def': 'E', 
    'DP_def': 'DP', 'fielding_perc': 'Fld%', 'bis_runs_total': 'Rdrs', 'bis_runs_total_per_season': 'Rdrs/yr', 
    'range_factor_per_nine': 'RF/9', 'range_factor_per_game': 'RF/G', 'fielding_perc_lg': 'lgFld%', 
    'range_factor_per_nine_lg': 'lgRF9', 'range_factor_per_game_lg': 'lgRFG', 'SB': 'SB', 'CS': 'CS', 
    'caught_stealing_perc': 'CS%', 'caught_stealing_perc_lg': 'lgCS%', 'pickoffs': 'PickOff', 
    'tz_runs_total': 'Rtot', 'tz_runs_total_per_season': 'Rtot/yr','PB': 'PB', 'WP': 'WP','award_summary': 'Awards',}

    std_table = []
    std_fielding_table = soup.find('table', attrs={'id':'standard_fielding'}).find('tbody')
    for row in std_fielding_table.findAll('tr', attrs={'id': re.compile('(\d{4}).standard_fielding')}):
        std = {}    
        y = row.find('th').text
        std['Year'] = int(y) if y.isnumeric() else y
        for col in row.findAll('td'):
            if f_std_heads.get(col['data-stat']) != None:
                std[f_std_heads[col['data-stat']]] = float(col.text) if col.text.isnumeric() else col.text
        std_table.append(std)
    
    std_fielding_foot = soup.find('table', attrs={'id':'standard_fielding'}).find('tfoot').find('tr')
    summary = {}
    summary['Year'] = int(re.search("\d+",std_fielding_foot.find('th').text).group(0))
    for col in std_fielding_foot.findAll('td'):
        if col['data-stat'] == "lg_ID":
            continue
        else:
            if f_std_heads.get(col['data-stat']) != None:
                summary[f_std_heads[col['data-stat']]] = float(col.text) if col.text.isnumeric() else col.text

    return std_table, summary



#f_std_heads = {'year_ID': 'Year', 'age': 'Age', 'team_ID': 'Tm', 'pos': 'Pos', 'lg_ID': 'Lg', 'G': 'G', 
#'GS': 'GS', 'CG': 'CG', 'Inn_def': 'Inn', 'chances': 'Ch', 'PO': 'PO', 'A': 'A', 'E_def': 'E', 
#'DP_def': 'DP', 'fielding_perc': 'Fld%', 'bis_runs_total': 'Rdrs', 'bis_runs_total_per_season': 'Rdrs/yr', 
#'range_factor_per_nine': 'RF/9', 'range_factor_per_game': 'RF/G', 'fielding_perc_lg': 'lgFld%', 
#'range_factor_per_nine_lg': 'lgRF9', 'range_factor_per_game_lg': 'lgRFG', 'SB': 'SB', 'CS': 'CS', 
#'caught_stealing_perc': 'CS%', 'caught_stealing_perc_lg': 'lgCS%', 'pickoffs': 'PickOff', 
#'tz_runs_total': 'Rtot', 'tz_runs_total_per_season': 'Rtot/yr','PB': 'PB', 'WP': 'WP','award_summary': 'Awards',}


#field_heads = ['Year', 'Age', 'Tm', 'Pos', 'Lg', 'G', 'GS', 'CG', 'Inn', 'Ch', 'PO', 'A', 'E', 'DP', 'Fld%',
# 'Rdrs', 'Rdrs/yr', 'RF/9', 'RF/G', 'lgFld%', 'lgRF9', 'lgRFG', 'SB', 'CS', 'CS%', 'lgCS%', 'PickOff', 'Awards']
#
#c = ['year_ID','age', 'team_ID', 'pos', 'lg_ID', 'G', 'GS', 'CG', 'Inn_def', 'chances', 'PO', 'A', 'E_def', 
#'DP_def', 'fielding_perc', 'bis_runs_total', 'bis_runs_total_per_season', 'range_factor_per_nine', 
#'range_factor_per_game', 'fielding_perc_lg', 'range_factor_per_nine_lg', 'range_factor_per_game_lg', 
#'SB', 'CS', 'caught_stealing_perc', 'caught_stealing_perc_lg', 'pickoffs', 'award_summary']


