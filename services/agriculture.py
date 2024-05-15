import os
import pandas as pd
from config import ROOT_DIR


dirname = os.path.dirname(os.path.abspath(__file__))



def crop_production_calculation():
    file_path = os.path.join(ROOT_DIR, "data/tests/crop-production.csv")    
    df = pd.read_csv(file_path, delimiter="\t", header=None)
    df = df.drop(df.index[0:15])
    df = df[0].str.split(',', expand=True)
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df.columns = ['year', "Corn", "color_0", "pen_down_0", 
                "year_1","Wheat", "color_1", "pen_down_1",
                "year_2","Soybean", "color_2", "pen_down_2",
                "year_3","SG", "color_3", "pen_down_3"]
    df.reset_index(drop=True, inplace=True)
    df['Corn'] = df['Corn'].str.replace('"', '').astype(int)
    df['Wheat'] = df['Wheat'].str.replace('"', '').astype(int)
    df['Soybean'] = df['Soybean'].str.replace('"', '').astype(int)
    df['SG'] = df['SG'].str.replace('"', '').astype(int)
    df = df[['year','Corn','Wheat','Soybean','SG']]

    crop_production_title = f'Crop Production (Bushels) - Start Year: 2008'
    temp = {"production": {
        'Year': df['year'].values.tolist(),
        'Corn': df['Corn'].values.tolist(),
        'Wheat': df['Wheat'].values.tolist(),
        'Soybean': df['Soybean'].values.tolist(),
        'SG': df['SG'].values.tolist(),
        "crop_production_title": crop_production_title
    }}
    return temp

def net_income_calculation():
    file_path = os.path.join(ROOT_DIR, "data/tests/ag-net-income.csv")
    df = pd.read_csv(file_path, delimiter="\t", header=None)
    df = df.drop(df.index[0:16])
    df = df[0].str.split(',', expand=True)
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df.columns = ['year', "Corn", "color_0", "pen_down_0", 
                "year_1","Wheat", "color_1", "pen_down_1",
                "year_2","Soybean", "color_2", "pen_down_2",
                "year_3","SG", "color_3", "pen_down_3",
                "year_4", "US$0", "color_4", "pen_down_4"]
    df.reset_index(drop=True, inplace=True)
    df['Corn'] = df['Corn'].str.replace('"', '').astype(float)
    df['Wheat'] = df['Wheat'].str.replace('"', '').astype(float)
    df['Soybean'] = df['Soybean'].str.replace('"', '').astype(float)
    df['SG'] = df['SG'].str.replace('"', '').astype(float)
    df['US$0'] = df['US$0'].str.replace('"', '').astype(float)
    df = df[['year','Corn','Wheat','Soybean','SG','US$0']]

    net_calculation_title  = f'Agriculture Net Income - Start Year: 2008'
    temp = {
        "Income": {
            'Year': df['year'].values.tolist(),
            'Corn': df['Corn'].values.tolist(),
            'US$0': df['US$0'].values.tolist(),
            'Wheat': df['Wheat'].values.tolist(),
            'Soybean': df['Soybean'].values.tolist(),
            'SG': df['SG'].values.tolist(),
            "netCalculationTitle": net_calculation_title
        }
    }
    return temp
