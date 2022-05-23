import bs4
import requests
import re
import csv
from time import sleep
from random import random
from os.path import getsize, exists
from player_scraper import player_scraper

_bref_url = "https://www.baseball-reference.com/"
_source = _bref_url + "players/"
_initials = "abcdefghijklmnopqrstuvwxyz"

patron = re.compile('(?P<name>[\s\.\w]+)(?P<hall>\+)?\s*\((?P<first_year>\d{4})-(?P<last_year>\d{4})\)')

_bio_headers = ['Name',"First year","Last year","Full Name","Country","Positions","Bat hand","Throw hand",
            "HoF","HoF type","HoF year","HoF comittee"]

batters_headers = ["Years","G","PA","AB","R","H","2B","3B","HR","RBI","SB","CS","BB","SO","BA","OBP","SLG",
    "OPS","OPS+","TB","GDP","HBP","SH","SF","IBB","Rbat","Rbaser","Rdp","Rfield","Rpos","RAA","WAA","Rrep",
    "RAR","WAR","waaWL%","162WL%","oWAR","dWAR","oRAR"]

pitchers_headers = ["Years","W","L","W-L%","ERA","G","GS","GF","CG","SHO","SV","IP","H","R","ER","HR",
    "BB","IBB","SO","HBP","BK","WP","BF","ERA+","FIP","WHIP","H9","HR9","BB9","SO9","SO/W","RA9","RA9opp",
    "RA9def","RA9role","PPFp","RA9avg","RAA","WAA","gmLI","WAAadj","WAR","RAR","waaWL%","162WL%"]


pitchers_file = 'data/pitchers.csv'
batters_file = 'data/batters.csv'
pit_bat_file = 'data/pit_bat.csv'
errors_Log = 'data/errors_log.txt'
finish_log = 'data/finish_log.txt'

e_l = open(errors_Log,'a',newline="")

f_l = open(finish_log,'r', newline="")
finish_players = str(f_l.read()).split('\n')
f_l.close()

f_l = open(finish_log,'a', newline="")

p_f =  open(pitchers_file, 'a', newline='') if exists(pitchers_file) else open(pitchers_file, 'w', newline='')
w_p_f = csv.DictWriter(p_f,_bio_headers + pitchers_headers)
if getsize(pitchers_file) == 0:
    w_p_f.writeheader()


b_f = open(batters_file, 'a', newline='') if exists(batters_file) else open(batters_file, 'w', newline='')
w_b_f = csv.DictWriter(b_f,_bio_headers +batters_headers)
if getsize(batters_file) == 0:
    w_b_f.writeheader()


p_b_f = open(pit_bat_file, 'a', newline='') if exists(pit_bat_file) else open(pit_bat_file, 'w', newline='')
w_p_b_f = csv.DictWriter(p_b_f,_bio_headers + pitchers_headers + [x+"_bat" for x in batters_headers])
if getsize(pit_bat_file) == 0:
    w_p_b_f.writeheader()

_players_count = 0

for ini in _initials:
    players_letter_url = _source + ini
    res = requests.get(players_letter_url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    players = soup.find('div', attrs = {'id':'div_players_'})
    for player in players.findAll('p'):
        _players_count +=1
        m =  patron.search(player.text)
        name = re.sub('\s([\s])+','',m.group('name'))
        if name in finish_players:
            continue
        vals = [name,int(m.group('first_year')),int(m.group('last_year'))]
        player_url = _bref_url + player.a['href']
        _player_type, stats = 0,[]
        try:
            _player_type, stats = player_scraper(player_url)
        except Exception as e:
            e_l.write(name + " : " + str(player_url)+"\n")
            print(" Error with player: " + name + " : " + str(player_url) + "..." + str(e) + "\n")
            continue
        
        vals.extend(stats)
        headers = []
        if _player_type == 1:
            w_p_f.writerow(dict(zip(_bio_headers +pitchers_headers,vals)))
        elif _player_type == 2:
            w_b_f.writerow(dict(zip(_bio_headers +batters_headers,vals)))
        else:
            w_p_b_f.writerow(dict(zip(_bio_headers + pitchers_headers + [x+"_bat" for x in batters_headers], vals)))
        if _players_count%250 == 0:
            print(f"in progress---{_players_count}")
        f_l.write(name+"\n")
       
        sleep(1.0+round(random()/1.3,4))

    print(f"{ini}--finish\n")
    sleep(1.0+round(random()/1.3,4))

p_f.close()
b_f.close()
p_b_f.close()
e_l.close()
f_l.close()
     