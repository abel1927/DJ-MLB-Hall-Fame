
positions = {'Pitcher':"P",
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
        'Pinch Runner':"PR",
        "P":'Pitcher',
            "OF":'Outfielder',
            "CF":'Centerfielder',
            "LF":'Leftfielder',
            "RF":'Rightfielder',
            "IF":'Infielder',
            "1B":'First Baseman',
            "3B":'Third Baseman',
             "C":'Catcher',
            "2B":'Second Baseman',
            "SS":'Shortstop',
            "PH":'Pinch Hitter',
            "DH":'Designated Hitter',
            "PR":'Pinch Runner'}

players_type= {
    1:"Pitcher",
    2:"Batter"
}

countries = {'af': "Afganistán",
     'as': "Samoa Americana",
     'at': "Austria",
     'au': "Australia",
     'aw': "Aruba",
     'be': "Bélgica",
     'br': "Brasil",
     'bs': "Bután",
     'bz': "Belice",
     'ca': "Canadá",
     'ch': "Suiza",
     'cn': "China",
     'co': "Colombia",
     'cu': "Cuba",
     'cw': "Curaçao",
     'cz': "República Checa",
     'de': "Alemania",
     'desconocido': "Desconocido",
     'dk': "Dinamarca",
     'do': "República Dominicana",
     'es': "España",
     'fi': "Finlandia",
     'fr': "Francia",
     'gb': "Reino Unido",
     'gr': "Grecia",
     'gu': "Guam",
     'hk': "Hong Kong",
     'hn': "Honduras",
     'id': "Indonesia",
     'ie': "Irlanda",
     'it': "Italia",
     'jm': "Jamaica",
     'jp': "Japón",
     'kr': "Corea del Sur",
     'lt': "Lituania",
     'lv': "Letonia",
     'mx': "México",
     'ni': "Nicaragua",
     'nl': "Países Bajos",
     'no': "Noruega",
     'pa': "Panamá",
     'pe': "Perú",
     'ph': "Filipinas",
     'pl': "Polonia",
     'pr': "Puerto Rico",
     'pt': "Portugal",
     'ru': "Rusia",
     'sa': "Arabia Saudí",
     'se': "Suecia",
     'sg': "Singapur",
     'sk': "Eslovaquia",
     'tw': "Taiwán",
     'ua': "Ucrania",
     'us': "Estados Unidos",
     've': "Venezuela",
     'vi': "Islas Vírgenes Americanas",
     'vn': "Vietnam",
     'za': "Sudáfrica"}

leagues_mayors =  {'AL','NL','AA','UA', 'PL','FL','NA'}

negro_leagues = {'ANL','ECL','EWL','NAL','NNL','NN2', 'NSL'}

headers_bio = ['Id', 'Name', 'Active','First year','Last year','Url','Country','Bat hand','Throw hand','Full Name','HoF','HoF type','HoF year','HoF comittee','Player type','retirement_age','total_seasons','career_teams','career_leagues','first_position','second_position','play_in_mayors','play_in_negro_league','two_way_player','debut_decade','retirament_decade']
headers_bat = ['2B_bt','3B_bt','AB_bt','BA_bt','BB_bt','CS_bt','G_bt','HR_bt','H_bt','IBB_bt','OBP_bt','OPS+_bt','OPS_bt','PA_bt','RAA_bt','RAR_bt','RBI_bt','R_bt','Rbaser_bt','Rbat_bt','Rdp_bt','Rfield_bt','Rpos_bt','Rrep_bt','SB_bt','SF_bt','SH_bt','SLG_bt','SO_bt','TB_bt','WAA_bt','WAR_bt','dWAR_bt','oRAR_bt','oWAR_bt','A_fd','CG_fd','CS%_fd','CS_fd','Ch_fd','DP_fd','E_fd','Fld%_fd','GS_fd','G_fd','Inn_fd','PB_fd','PO_fd','RF/9_fd','RF/G_fd','SB_fd','WP_fd']
headers_pit = ['W_pt','L_pt','W-L%_pt','ERA_pt','G_pt','GS_pt','GF_pt','CG_pt','SHO_pt','SV_pt','IP_pt','H_pt','R_pt','ER_pt','HR_pt','BB_pt','IBB_pt','SO_pt','HBP_pt','BK_pt','WP_pt','BF_pt','ERA+_pt','FIP_pt','WHIP_pt','H9_pt','HR9_pt','BB9_pt','SO9_pt','SO/W_pt','RAA_pt','WAA_pt','WAR_pt','RAR_pt']

bat_basic_stats = ['2B_bt','3B_bt','AB_bt','BB_bt','CS_bt','G_bt','HR_bt','H_bt','IBB_bt','PA_bt','RBI_bt','R_bt','SB_bt','HBP_bt','SF_bt','SH_bt','SO_bt']
bat_calc_stats = ['BA_bt', 'OBP_bt','OPS_bt','SLG_bt','TB_bt']
bat_adv_stats = ['OPS+_bt', 'RAA_bt','RAR_bt','Rbaser_bt','Rbat_bt','Rdp_bt','Rfield_bt','Rpos_bt','Rrep_bt', 'WAA_bt','WAR_bt','dWAR_bt','oRAR_bt','oWAR_bt']

field_basic_stats = ['A_fd','CG_fd','CS_fd','DP_fd','E_fd','GS_fd','G_fd','Inn_fd','PB_fd','PO_fd','SB_fd','WP_fd']
field_calc_stats = ['Ch_fd','Fld%_fd']

pit_basic_stats = ['W_pt','L_pt','G_pt','GS_pt','GF_pt','CG_pt','SHO_pt','SV_pt','IP_pt','H_pt','R_pt','ER_pt','HR_pt','BB_pt','IBB_pt','SO_pt','HBP_pt','BK_pt','WP_pt','BF_pt']
pit_calc_stats = ['W-L%_pt','ERA_pt','FIP_pt','WHIP_pt','H9_pt','HR9_pt','BB9_pt','SO9_pt','SO/W_pt']
pit_adv_stats = ['ERA+_pt','RAA_pt','WAA_pt','WAR_pt','RAR_pt']

def get_position_by_reverse_key(pos_name_or_key:str)->str:
    return positions[pos_name_or_key]

def get_player_type_by_key(key:int)->str:
    return players_type[key]

def get_decade(year:float)->int:
    return year-(year%10)

def get_country_by_key(key:str)->str:
    return countries[key]