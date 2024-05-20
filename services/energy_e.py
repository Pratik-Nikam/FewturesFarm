import os
import pandas as pd
import json
from config import ROOT_DIR

dirname = os.path.dirname(os.path.abspath(__file__))


dirname = os.path.dirname(__file__)
def farm_energy_production_calculation(key=None):
    file_path =file_path = os.path.join(ROOT_DIR, f"data/outputs/{key}/farm-energy-production.csv")
    farm_energy_production_data = pd.read_csv(file_path, delimiter="\t", header=None)

    # Preprocess the DataFrame
    df = pd.DataFrame(farm_energy_production_data)


    df = df.drop(df.index[0:14])
    df = df[0].str.split(',', expand=True)
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df.columns = ['year', "Wind", "color_0", "pen_down_0", 
                "year_1","Solar", "color_1", "pen_down_1",
                "year_2","0 MWh", "color_2", "pen_down_2"]

    # Reset the index
    df.reset_index(drop=True, inplace=True)

    # Convert columns to integers
    df['Wind'] = df['Wind'].str.replace('"', '').astype(float)
    df['Solar'] = df['Solar'].str.replace('"', '').astype(float)
    df['0 MWh'] = df['0 MWh'].str.replace('"', '').astype(float)

    df=df[['year','Wind','Solar','0 MWh']]

    farmenergyproductiontitle = f'Farm Energy Net Production- Start Year: 2008 (Comination: {key})'

    temp = {"energy": {
        'Year': df['year'].values.tolist(),
        'Wind': df['Wind'].values.tolist(),
        'Solar': df['Solar'].values.tolist(),
        'zeroMWh': df['0 MWh'].values.tolist(),
        'farmenergyproductiontitle':farmenergyproductiontitle
    }}
    return json.dumps(temp)


def energy_net_income_calculation(key=None):

    file_path =file_path = os.path.join(ROOT_DIR, f"data/outputs/{key}/energy-net-income.csv")
 
    energy_net_income_data = pd.read_csv(file_path, delimiter="\t", header=None)

    df = energy_net_income_data

    df = df.drop(df.index[0:14])

    df = df[0].str.split(',', expand=True)

    df.columns = df.iloc[0]
    df = df.iloc[1:]

    df.columns = ['year', "Wind", "color_0", "pen_down_0", 
                "year_1","Solar", "color_1", "pen_down_1",
                "year_2","US$0", "color_2", "pen_down_2"]

    # Reset the index
    df.reset_index(drop=True, inplace=True)

    df['Wind'] = df['Wind'].str.replace('"', '')


    df['Wind'] = df['Wind'].str.replace('"', '').astype(float)

    df['Solar'] = df['Solar'].str.replace('"', '').astype(float)

    df['US$0'] = df['US$0'].str.replace('"', '').astype(float)

    df=df[['year','Wind','Solar','US$0']]

    energyproductiontitle = f'Farm Energy Net Income - Start Year: 2008 (Comination: {key})'


    temp = {
        "Income": {
            'Year': df['year'].values.tolist(),
            'Wind': df['Wind'].values.tolist(),
            'US$0': df['US$0'].values.tolist(),
            'Solar': df['Solar'].values.tolist(),
            'energyproductiontitle':energyproductiontitle
        }
    }

    return json.dumps(temp)

