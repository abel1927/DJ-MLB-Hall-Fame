import bs4
import requests
import re
import json
from time import sleep
from random import random
from os import mkdir
from os.path import exists
from player_scraper import player_scraper

_bref_url = "https://www.baseball-reference.com/"
_source = _bref_url + "players/"
_initials = "abcdefghijklmnopqrstuvwxyz"

patron = re.compile('(?P<name>[\s\.\w]+)(?P<hall>\+)?\s*\((?P<first_year>\d{4})-(?P<last_year>\d{4})\)')

#general_data = './Data/players_mlb.json'

all_data = './Data/players/'

errors_Log = './Data/errors_log.txt'
finish_log = './Data/finish_log.txt'

e_l = open(errors_Log,'a',newline="")

f_l = open(finish_log,'r', newline="")
finish_players = str(f_l.read()).split('\n')

f_l.close()

f_l = open(finish_log,'a', newline="")

_players_count = len(finish_players)

for ini in _initials:
    ini_path = all_data + ini
    if not exists(ini_path):
        mkdir(ini_path)

    ini_htmls_path = ini_path+'/html'
    ini_jsons_path = ini_path+'/json'

    if not exists(ini_htmls_path):
        mkdir(ini_htmls_path)
    if not exists(ini_jsons_path):
        mkdir(ini_jsons_path)

    players_letter_url = _source + ini
    res = requests.get(players_letter_url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    players = soup.find('div', attrs = {'id':'div_players_'})
    for player in players.findAll('p'):
        initial_attr = {}
        m =  patron.search(player.text)
        name = re.sub('\s([\s])+','',m.group('name'))
        if name in finish_players:
            continue
        id = name+"_"+str(_players_count)
        initial_attr['Id'] = id.replace(" ", "_")
        initial_attr['Name'] = name
        initial_attr['Active'] = player.find('b')!= None
        initial_attr['First year'], initial_attr['Last year'] = int(m.group('first_year')),int(m.group('last_year'))
        player_url = _bref_url + player.a['href']
        initial_attr['Url'] = player_url
        try:
            player_dict = player_scraper(player_url, initial_attr, save_html=False, html_save_path=ini_htmls_path+"/"+initial_attr['Id']+".txt")
            with open(ini_jsons_path+"/"+initial_attr['Id']+'.json', 'w') as file:
                json.dump(player_dict, file, indent=4)
        except Exception as e:
            e_l.write(name + " : " + str(player_url)+"\n")
            print(" Error with player: " + name + " : " + str(player_url) + "..." + str(e) + "\n")
            continue
        
        if _players_count%15 == 0:
            print(f"in progress---{_players_count}")
        f_l.write(name+"\n")
        _players_count +=1
       
        sleep(1.0+round(random()/1.3,4))

    print(f"{ini}--finish\n")
    sleep(1.0+round(random()/1.3,4))

e_l.close()
f_l.close()
     