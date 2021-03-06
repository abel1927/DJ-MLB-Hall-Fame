
def pitcher_seasson_avg_Calc(stat, games_plus_games_started, seasson_factor=68,r=0):
    player_factor = games_plus_games_started/seasson_factor
    return round((stat/player_factor),r)

def win_lose_percentage(wins,loses):
    return round(wins/(wins+loses),3) if (wins+loses) != 0 else 0

def era(er,ip):
    return round(er/ip,3) if ip != 0 else 0

def fip(hr,bb,hbp,so,ip):
    return round((13*hr+3*(bb+hbp)-2*so)/ip,2) if ip != 0 else 0

def whip(bb,h,ip):
    return round((bb+h)/ip,3) if ip != 0 else 0

def h9(h,ip):
    return round((h/ip)*9,3) if ip != 0 else 0

def hr9(hr,ip):
    return round((hr/ip)*9,3) if ip != 0 else 0

def bb9(bb,ip):
    return round((bb/ip)*9,3) if ip != 0 else 0

def so9(so,ip):
    return round((so/ip)*9,3) if ip != 0 else 0

def soW(so,w):
    return round((so/w),3) if w != 0 else 0

def runs_better_than_average(ip,ra9_average,ra9):
    return round(ip*(ra9_average-ra9)/9,3) if ip != 0 else 0

def era_plus(era,era_league_average):
    return round(100*era_league_average/era,3) if era != 0 else 0