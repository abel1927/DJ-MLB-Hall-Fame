def win_lose_percentage(wins,loses):
    return round(wins/(wins+loses),3) if (wins+loses) != 0 else 0

def era(er,ip):
    return round(er/ip,3) if ip != 0 else 0

def filder_independent_pitching_rating(hr,bb,hbp,so,ip,constant_lg):
    return round((13*+3*(bb+hbp+so)-2*so)/ip+constant_lg,2) if ip != 0 else 0

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

#????????????
def wins_above_average(waaWL_percent,games):
    pass

#????????????
def war(args):
    pass