from typing import Dict, List
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from data_keys import steroid_reports_players

def select_features(df:pd.DataFrame, features:List)->pd.DataFrame:
    return df[features]

def filter_dataset(df:pd.DataFrame==None, eq_conditions:Dict==None, 
gt_conditions:Dict==None,lt_conditions:Dict==None, ineq_conditions:Dict==None)->pd.DataFrame:
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

def encode_features(df: pd.DataFrame, features: List[str]):
    for feat in features:
        df[feat] = df[feat].astype('category')
        le = LabelEncoder()
        df[feat] = le.fit_transform(df[feat])

def separete_steroids_players(df:pd.DataFrame):
    steroid_p_url = steroid_reports_players.values()
    steroid_idx = df[df["Url"] in steroid_p_url].index
    with_out_steroid_p_df = df.drop(steroid_idx)
    steroid_p_df =  df.iloc[steroid_idx]
    return with_out_steroid_p_df, steroid_p_df