
#"Ch"
def defensive_chaces(putout, assists, errors):
    return putout+assists+errors

#"Fld%"
def fielding_percentage(putout, assists, errors):
    num = putout+assists
    den = putout+assists+errors
    return round(num/den,3) if den != 0 else 0

#"RF/9"
def range_factor_per_9_inng(putout, assists, inn):
    num = 9*(putout+assists)
    den = inn
    return round(num/den,2) if den != 0 else 0

#"RF/G"
def range_factor_per_game(putout, assists, gplayed):
    num = putout+assists
    den = gplayed
    return round(num/den,2) if den != 0 else 0

#"CS%"
def caught_stealing_percentage(stolen_bases, caught_stealing):
    num = caught_stealing
    den = stolen_bases+caught_stealing
    return round(num/den,1) if den != 0 else 0

def inning_sum(new_inn:float, curr_inn:float)->float:
    new_inn_int, new_inn_dec = int(new_inn), round(new_inn%1,1)
    curr_inn_int, curr_inn_dec = int(curr_inn), round(curr_inn%1,1)
    inn_int = new_inn_int + curr_inn_int
    inn_dec = 10*(new_inn_dec+curr_inn_dec)
    inn = inn_int + (inn_dec//3) + (inn_dec%3/10)
    return inn

