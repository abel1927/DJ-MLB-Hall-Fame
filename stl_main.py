import streamlit as st
from pickle import load
import pandas as pd
import json

from Preprocessing.data_frame_procces import select_features

def title():
    st.markdown(
    "<h1 style='text-align: center; '>DJ MLB Hall of Fame</h1>",
    unsafe_allow_html=True,)

def filter_dataset(df:pd.DataFrame=None, eq_conditions=None, 
gt_conditions=None,lt_conditions=None, ineq_conditions=None)->pd.DataFrame:
    if eq_conditions != None:
        for cond_key in eq_conditions.keys():
            cond_value = eq_conditions[cond_key]
            df = df[df[cond_key].isin(cond_value)]
    if gt_conditions != None:
        for cond_key in gt_conditions.keys():
            cond_value = gt_conditions[cond_key]
            df = df[df[cond_key]>=cond_value]
    if lt_conditions != None:
        for cond_key in lt_conditions.keys():
            cond_value = lt_conditions[cond_key]
            df = df[df[cond_key]<=cond_value]
    if ineq_conditions != None:
        for cond_key in ineq_conditions.keys():
            cond_value = ineq_conditions[cond_key]
            df = df[~df[cond_key].isin(cond_value)]
    return df

def load_batter_model():
    path = 'Models/trained_models/batter_career_log_reg_std_model.pkl'
    model_ = None
    with open(path, 'rb') as file:
        model_= load(file)
    return model_

def load_pitcher_model():
    path = 'Modelsb/models_trained/svm_lda_model.pkl'
    model_ = None
    with open(path, 'rb') as file:
        model_= load(file)
    return model_

def load_batter_df():
    bat_df = pd.read_csv("Data/Corpus_csv/batters_all_career.csv")
    bat_df['retirement_age'] = (
        bat_df['retirement_age'].replace('desconocido', bat_df['retirement_age'].mode()[0])
    )
    bat_df['retirement_age'] = bat_df['retirement_age'].astype('int64')
    eq_conditions = {
        "Active":[False],
        "HoF type":['-','Player']
    }

    gt_conditions = {
        'retirament_decade':2009,
        "total_seasons":10,
    }
    bat_df = filter_dataset(bat_df, eq_conditions, gt_conditions, None, None)
    bat_df.reset_index(inplace=True, drop=True)
    return  bat_df

def load_pitcher_df():
    pit_df = pd.read_csv("Data/Corpus_csv/pitchers_all_career.csv")
    pit_df['retirement_age'] = (
        pit_df['retirement_age'].replace('desconocido', pit_df['retirement_age'].mode()[0])
    )
    pit_df['retirement_age'] = pit_df['retirement_age'].astype('int64')
    eq_conditions = {
        "Active":[False],
        "HoF type":['-','Player']
    }

    gt_conditions = {
        'retirament_decade':2009,
        "total_seasons":10,
    }
    pit_df = filter_dataset(pit_df, eq_conditions, gt_conditions, None, None)
    pit_df.reset_index(inplace=True, drop=True)
    return pit_df

def load_bat_features():
    f = ["retirement_age","total_seasons","WAR_bt", "SLG_bt",
        "OBP_bt", "2B_bt","3B_bt","R_bt", "Rfield_bt","RBI_bt", "G_bt","HR_bt","H_bt", 
        "SB_bt", "Rbaser_bt", "Rrep_bt", "Rbat_bt"]
    return f

def load_pit_features():
    f = ["total_seasons","WAR_pt", "WHIP_pt", "ERA_pt", "BB_pt","G_pt","W-L%_pt",
    "R_pt","SHO_pt","H_pt" ,"RAA_pt"]
    return f

def load_keys(df):
    name = df['Name'].to_numpy()
    id = df['Id'].to_numpy()
    keys = {name[i]:id[i] for i in range(len(name))}
    return keys

def show_tops():
    st.info("Result of models this was a top players")
    st.write()
    st.markdown(
    "<h3>Pitchers Top</h1>",unsafe_allow_html=True,)
    pit = [('Mariano Rivera', 0.85, 1),('Roy Halladay', 0.72, 1),('CC Sabathia', 0.611, 0),('Trevor Hoffman', 0.034, 1)]
    for p in pit:
        st.write(f"{p[0]}----> Probability:{p[1]}------>Current status: {p[2]}")

    st.write()
    st.write()
    st.markdown(
    "<h3>Batters Top</h1>",unsafe_allow_html=True,)
    bat = [('Alex Rodriguez', 1.0, 0),('Adrian Beltre', 0.991, 0),('Chipper Jones', 0.989, 1),('Ken Griffey Jr.', 0.985, 1),('Derek Jeter', 0.949, 1),('Ivan Rodriguez', 0.882, 1),('Carlos Beltran', 0.877, 0),('Ichiro Suzuki', 0.861, 0),('Scott Rolen', 0.858, 0),('Chase Utley', 0.825, 0),('Manny Ramirez', 0.819, 0),('Vladimir Guerrero', 0.792, 1),('Todd Helton', 0.774, 0),('Andruw Jones', 0.585, 0),('Jim Thome', 0.582, 1),('David Ortiz', 0.061, 1)]
    for p in bat:
        st.write(f"{p[0]}----> Probability:{p[1]}------>Current status: {p[2]}")

    st.write()
    st.write()
    st.info("David Ortiz and Trevor Hoffman have been dropped by the model, but...a little danger, sorry Big Papy..")

def get_proba():
    search = st.text_input('Player name', value=st.session_state.last_search)
    if st.button('Calculate'):
        if search == "":
            st.warning("A player name is required")
        else:
            with st.spinner('Wait for it...'):
                p_name = search
                p_id = ""
                for k in st.session_state.bat_keys.keys():
                    if k == p_name:
                        p_id = st.session_state.bat_keys[k]
                        break
                if p_id != "":
                    b_df = st.session_state.batter_df
                    _idx = b_df[b_df["Id"]==p_id].index
                    p_df =  b_df.iloc[_idx]
                    p_df = select_features(p_df, st.session_state.bat_features)
                    _model = st.session_state.batter_model
                    pred = _model.predict_proba(p_df)
                    result = round(pred[0][1],3)
                    st.write(f"{p_name} --->  HoF inclusion probability:{result}")
                else:
                    for k in st.session_state.pit_keys.keys():
                        if k == p_name:
                            p_id = st.session_state.pit_keys[k]
                            break
                    if p_id != "":
                        pit_df = st.session_state.pitcher_df
                        _idx = pit_df[pit_df["Id"]==p_id].index
                        p_df =  pit_df.iloc[_idx]
                        p_df = select_features(p_df, st.session_state.pit_features)
                        _model = st.session_state.pitcher_model
                        pred = _model.predict_proba(p_df)
                        result = round(pred[0][1],3)
                        st.write(f"{p_name} --->  HoF inclusion probability:{result}")
                    else:
                        st.info("""The player's name is incorrect or you have selected a player who does not meet the selection 
                        criteria for the Hall of Fame.
                        Remember that he must be retired and have played at least 10 years in the major leagues, 
                        with at least one of them falling within the 15-year period prior to the election.""")

if __name__ == '__main__':

    if not 'batter_model' in st.session_state:
        _model = load_batter_model()
        st.session_state.batter_model = _model
    if not 'pitcher_model' in st.session_state:
        _model = load_pitcher_model() 
        st.session_state.pitcher_model = _model
    if not 'batter_df' in st.session_state:
        st.session_state.batter_df = load_batter_df()
    if not 'pitcher_df' in st.session_state:
        st.session_state.pitcher_df = load_pitcher_df()
    if not 'bat_features' in st.session_state:
        st.session_state.bat_features = load_bat_features()
    if not 'pit_features' in st.session_state:
        st.session_state.pit_features = load_pit_features()
    if not 'bat_keys' in st.session_state:
        st.session_state.bat_keys = load_keys(st.session_state.batter_df) 
    if not 'pit_keys' in st.session_state:
        st.session_state.pit_keys = load_keys(st.session_state.pitcher_df)
    if not 'last_search' in st.session_state:
        st.session_state.last_search  = ""

    st.set_page_config(
        page_title="DJ MLB Hall Of Fame Page")

    st.sidebar.header('DJ MLB Hall Of Fame, A data journalism and ML proyect')
    nav = st.sidebar.radio('',['Probability Pred', 'Display Tops'])
    st.sidebar.markdown(""" \n \n""")

    st.sidebar.markdown(" ## [Source Code](https://github.com/abel1927/DJ-MLB-Hall-Fame)", unsafe_allow_html=True,)
    st.sidebar.markdown(""" \n""")

    expander = st.sidebar.expander('Team')
    expander.markdown("### We are students of CS at the MATCOM faculty of Havana University.\n #### Julio J. Horta Vázquez [Belzico] (https://github.com/Belzico)\n #### Abel Molina Sánchez [abel1927] (https://github.com/abel1927)", unsafe_allow_html=True,)
    
    title()
    if nav == 'Probability Pred':
        get_proba()
    else:  
        show_tops()