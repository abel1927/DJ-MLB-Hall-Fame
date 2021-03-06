
def batter_seasson_avg_Calc(stat, games, seasson_factor=164,r=0):
    player_factor = games/seasson_factor
    return round((stat/player_factor),r)

def plate_appereance(at_bat, base_on_balls,hit_by_pitch,sacrife_flies,sacrifice_bunts):
    plate_appereance=at_bat+base_on_balls+hit_by_pitch+sacrife_flies+sacrifice_bunts
    return plate_appereance
    
def batting_average(hits,at_bat):
    return round(hits/at_bat,3) 

def batting_obp(hits,base_on_balls,hbp,at_bat,sacrifice_flies):
    return round((hits+base_on_balls+hbp)/(at_bat+base_on_balls+hbp+sacrifice_flies),3)

def slugger(singles,doubles,triples,hr,at_bat):
    return round((singles+2*doubles+3*triples+4*hr)/at_bat,3)

def batting_ops(on_base,slugging_perc):
    return round(on_base+slugging_perc,3)

def total_bases(singles,doubles,triples,hr):
    return round(singles+2*doubles+3*triples+4*hr,3)