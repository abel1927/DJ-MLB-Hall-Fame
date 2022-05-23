from typing import Tuple
from bs4 import BeautifulSoup, Comment
import requests
import re

def player_scraper(url:str)->Tuple[int,list]: 

    pos = ['Pitcher','Outfielder', 'Centerfielder', 'Leftfielder', 'Rightfielder','Infielder', 'First Baseman', 
    'Third Baseman', 'Catcher', 'Second Baseman', 'Shortstop', 'Pinch Hitter', 'Designated Hitter', "Pinch Runner"]

    hands = ['Left','Right','Both']

    #player_bio_header = ["Full Name","Country","Positions","Bat hand","Throw hand","HoF","HoF type","HoF year","HoF comittee"]
    player_bio_stats = []
    
    bat_standard_stats = []
    bat_value_stats = []

    pit_standard_stats = []
    pit_value_stats = []

    #1 -- pitcher 2-- batter 3-- both
    _player_type = 0
    _vals = []

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    nationality = ''
    positions = []
    bat,throw = '-','-'
    fname = ''
    hof,hof_type,hof_year,hof_comittee = '-','-','-', '-'

    for data in soup.findAll('p'):
        if 'Born:' in data.text:
            born = data.find('span',  attrs = {'class': re.compile('f-i f-')})
            nationality = born.text if born != None else ""
        elif re.search("Position(s)?", data.text):
            for p in pos:
                if p in data.text:
                    positions.append(p)
        elif 'Bats:' in data.text:
            temp = data.text
            _len = len(temp)
            for h in hands:
                if h in temp[:_len//2]:
                    bat = h
                if h in temp[_len//2:]:
                    throw = h
        elif 'Full Name:' in data.text:
            fname = re.sub("^\s+|\s+$","",data.text.replace("Full Name:", "").replace("\n",""))
        elif 'Hall of Fame:' in data.text:
            temp = data.text.replace("Hall of Fame:","")
            _patron = re.compile('(View)(.*)')
            temp = _patron.sub("", temp)
            hof = 1
            hof_type = re.search("[Pp]layer|[Mm]anager|Pioneer/Executive|Umpire", temp).group(0)
            hof_year = re.search("\d{4}", temp).group(0)
            hof_comittee = re.search("Voted by (?P<entity>Special Election|Old Timers Committee|Negro League Committee|Veteran's Committee|BBWAA|Centennial Committee)",temp).group('entity')

    player_bio_stats = [fname,nationality,positions,bat,throw,hof,hof_type,hof_year,hof_comittee]

    if 'Pitcher' in positions:
        _player_type +=1
        try:
            std_in_comment = soup.find('table', attrs={'id':'pitching_standard'}) == None
            if not std_in_comment: 
                std_pitching_table = soup.find('table', attrs={'id':'pitching_standard'}).find('tfoot').find('tr')
                pit_standard_stats.append(std_pitching_table.find('th').text)
                for col in std_pitching_table.findAll('td'):
                    if col['data-stat'] == "lg_ID":
                        continue
                    else:
                        pit_standard_stats.append(col.text)
        except Exception as e:
            print(fname+ "pit-exception-blok1")
            raise(e)
        try:
            for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
                if comment.find('table ') > 0:
                    comment_soup = BeautifulSoup(comment, 'html.parser')
                    if comment_soup.find('table', attrs={'id':'pitching_value'}) != None:
                        val_pitching_table = comment_soup.find('table', attrs={'id':'pitching_value'}).find('tfoot').find('tr')
                        pit_value_stats.append(val_pitching_table.find('th').text)
                        for col in val_pitching_table.findAll('td'):
                            if col['data-stat'] == "lg_ID":
                                continue
                            else:
                                pit_value_stats.append(col.text)
                    elif std_in_comment and comment_soup.find('table', attrs={'id':'pitching_standard'}) != None:
                        std_pitching_table = comment_soup.find('table', attrs={'id':'pitching_standard'}).find('tfoot').find('tr')
                        pit_standard_stats.append(std_pitching_table.find('th').text)
                        for col in std_pitching_table.findAll('td'):
                            if col['data-stat'] == "lg_ID":
                                continue
                            else:
                                pit_standard_stats.append(col.text)
        except Exception as e:
            print(fname+ "pit-exception-blok2")
            raise(e)
        try:
            pit_standard_stats[0] = re.search("\d+",pit_standard_stats[0]).group(0)
            pit_standard_stats = [float(x) if x.isnumeric() else x for x in pit_standard_stats[:-1]]
            pit_value_stats = [float(x) if x.isnumeric() else x for x in pit_value_stats[5:-2]]
            _vals = player_bio_stats + pit_standard_stats + pit_value_stats
        except Exception as e:
            print(fname+ "pit-exception-blok3")
            raise(e)
    if not 'Pitcher' in positions or len(positions)>1:
        _player_type +=2
        try:
            std_in_comment = soup.find('table', attrs={'id':'batting_standard'}) == None
            if not std_in_comment:
                std_batting_table = soup.find('table', attrs={'id':'batting_standard'}).find('tfoot').find('tr')
                bat_standard_stats.append(std_batting_table.find('th').text)
                for col in std_batting_table.findAll('td'):
                    if col['data-stat'] == "lg_ID":
                        continue
                    else:
                        bat_standard_stats.append(col.text)
        except Exception as e:
            print(fname+"bat-exception-blok1")
            raise e
        try:
            for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
                if comment.find('table ') > 0:
                    comment_soup = BeautifulSoup(comment, 'html.parser')
                    if comment_soup.find('table', attrs={'id':'batting_value'}) != None:
                        val_batting_table = comment_soup.find('table', attrs={'id':'batting_value'}).find('tfoot').find('tr')
                        bat_value_stats.append(val_batting_table.find('th').text)
                        for col in val_batting_table.findAll('td'):
                            if col['data-stat'] == "lg_ID":
                                continue
                            else:
                                bat_value_stats.append(col.text)
                    elif std_in_comment and comment_soup.find('table', attrs={'id':'batting_standard'}) != None:
                        std_batting_table = comment_soup.find('table', attrs={'id':'batting_standard'}).find('tfoot').find('tr')
                        bat_standard_stats.append(std_batting_table.find('th').text)
                        for col in std_batting_table.findAll('td'):
                            if col['data-stat'] == "lg_ID":
                                continue
                            else:
                                bat_standard_stats.append(col.text)
        except Exception as e:
            print(fname+"bat-exception-blok2")
            raise e
        try:
            bat_standard_stats[0] = re.search("\d+",bat_standard_stats[0]).group(0)
            bat_standard_stats = [float(x) if x.isnumeric() else x for x in bat_standard_stats[:-2]]
            bat_value_stats = [float(x) if x.isnumeric() else x for x in bat_value_stats[3:-3]]
            if _player_type == 2:
                _vals = player_bio_stats + bat_standard_stats + bat_value_stats
            else:
                _vals.extend(bat_standard_stats+bat_value_stats)
        except Exception as e:
            print(fname+"bat-exception-blok3")
            raise e

    return _player_type, _vals
