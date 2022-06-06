from typing import Dict
from bs4 import BeautifulSoup, Comment
import requests
import re
from utils_tables_scraper import *


def get_bio(soup, player_dict):

    pos = ['Pitcher','Outfielder', 'Centerfielder', 'Leftfielder', 'Rightfielder','Infielder', 'First Baseman', 
    'Third Baseman', 'Catcher', 'Second Baseman', 'Shortstop', 'Pinch Hitter', 'Designated Hitter', "Pinch Runner"]

    hands = ['Left','Right','Both']

    player_dict['Country'] = "desconocido"
    player_dict['Positions'] = []
    player_dict['Bat hand'] ,player_dict['Throw hand'] = "desconocido","desconocido"
    player_dict['Full Name'] = "desconocido"
    player_dict['HoF'] = 0
    player_dict['HoF type'] = "-"
    player_dict['HoF year'] = '-'
    player_dict['HoF comittee'] = '-'

    for data in soup.findAll('p'):
        if 'Born:' in data.text:
            born = data.find('span',  attrs = {'class': re.compile('f-i f-')})
            player_dict['Country'] = born.text if born != None else ""
        elif re.search("Position(s)?", data.text):
            for p in pos:
                if p in data.text:
                    player_dict['Positions'].append(p)
        elif 'Bats:' in data.text:
            temp = data.text
            _len = len(temp)
            for h in hands:
                if h in temp[:_len//2]:
                    player_dict['Bat hand'] = h
                if h in temp[_len//2:]:
                    player_dict['Throw hand'] = h
        elif 'Full Name:' in data.text:
            player_dict['Full Name'] = re.sub("^\s+|\s+$","",data.text.replace("Full Name:", "").replace("\n",""))
        elif 'Hall of Fame:' in data.text:
            temp = data.text.replace("Hall of Fame:","")
            _patron = re.compile('(View)(.*)')
            temp = _patron.sub("", temp)
            player_dict['HoF'] = 1
            player_dict['HoF type'] = re.search("[Pp]layer|[Mm]anager|Pioneer/Executive|Umpire", temp).group(0)
            player_dict['HoF year'] = re.search("\d{4}", temp).group(0)
            player_dict['HoF comittee'] = re.search("Voted by (?P<entity>Special Election|Old Timers Committee|Negro League Committee|Veteran's Committee|BBWAA|Centennial Committee)",temp).group('entity')

    return player_dict



def player_scraper(url:str, initial_attr:Dict, save_html:bool=False, html_save_path:str="")->Dict: 

    #1 -- pitcher 2-- batter 3-- both
    _player_type = 0

    player_dict = initial_attr.copy()

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    player_dict = get_bio(soup=soup, player_dict=player_dict)
    player_dict['batter_stats'] = {}
    player_dict['pitcher_stats'] = {}
    player_dict['field_stats'] = {}
    
    if 'Pitcher' in player_dict['Positions']:
        _player_type +=1
        try:
            std_in_comment = soup.find('table', attrs={'id':'pitching_standard'}) == None
            if not std_in_comment: 
                by_years, summary = get_standard_pitching_table(soup=soup)
                player_dict['pitcher_stats']['standard_stats'] = {"by_years":by_years,'summary':summary}
        except Exception as e:
            print(player_dict['Full Name']+ "pit-exception-blok1")
            raise(e)
        try:
            for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
                if comment.find('table ') > 0:
                    comment_soup = BeautifulSoup(comment, 'html.parser')
                    if comment_soup.find('table', attrs={'id':'pitching_value'}) != None:
                        by_years, summary = get_value_pitching_table(soup=comment_soup)
                        player_dict['pitcher_stats']['value_stats'] = {"by_years":by_years,'summary':summary}
                    elif std_in_comment and comment_soup.find('table', attrs={'id':'pitching_standard'}) != None:
                        by_years, summary = get_standard_pitching_table(soup=comment_soup)
                        player_dict['pitcher_stats']['standard_stats'] = {"by_years":by_years,'summary':summary}
        except Exception as e:
            print(player_dict['Full Name']+ "pit-exception-blok2")
            raise(e)
    if not 'Pitcher' in player_dict['Positions'] or len(player_dict['Positions'])>1:
        _player_type +=2
        try:
            std_in_comment = soup.find('table', attrs={'id':'batting_standard'}) == None
            if not std_in_comment:
                by_years, summary = get_standard_batting_table(soup=soup)
                player_dict['batter_stats']['standard_stats'] = {"by_years":by_years,'summary':summary}
            field_in_comment = soup.find('table', attrs={'id':'standard_fielding'}) == None
            if not field_in_comment:
                by_years, summary = get_standard_fielding_table(soup=soup)
                player_dict['field_stats'] = {"by_years":by_years,'summary':summary}
        except Exception as e:
            print(player_dict['Full Name']+"bat-exception-blok1")
            raise e
        try:
            for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
                if comment.find('table ') > 0:
                    comment_soup = BeautifulSoup(comment, 'html.parser')
                    if comment_soup.find('table', attrs={'id':'batting_value'}) != None:
                        by_years, summary = get_value_batting_table(soup=comment_soup)
                        player_dict['batter_stats']['value_stats'] = {"by_years":by_years,'summary':summary}
                    elif std_in_comment and comment_soup.find('table', attrs={'id':'batting_standard'}) != None:
                        by_years, summary = get_standard_batting_table(soup=comment_soup)
                        player_dict['batter_stats']['standard_stats'] = {"by_years":by_years,'summary':summary}
                    elif field_in_comment and comment_soup.find('table', attrs={'id':'standard_fielding'}) != None:
                        by_years, summary = get_standard_fielding_table(soup=comment_soup)
                        player_dict['field_stats'] = {"by_years":by_years,'summary':summary}
        except Exception as e:
            print(player_dict['Full Name']+"bat-exception-blok2")
            raise e

    player_dict['Player type'] = _player_type
    if save_html:
        with open(html_save_path,'w') as f:
            f.write(res.text)

    return player_dict