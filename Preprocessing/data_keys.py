
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
    2:"Batter",
    3:"Pitcher_Batter"
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

def get_position_by_reverse_key(pos_name_or_key:str)->str:
    return positions[pos_name_or_key]

def get_player_type_by_key(key:int)->str:
    return players_type[key]

def get_decade(year:float)->int:
    return year-(year%10)

def get_country_by_key(key:str)->str:
    return countries[key]