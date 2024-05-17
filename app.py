from flask import Flask, render_template, request, jsonify, send_file, session
import os
import pandas as pd
import json

from config import ROOT_DIR

from services import climate_c, energy_e, water_w, agriculture_a, get_combination

app = Flask(__name__, template_folder='template')
app.secret_key = b'\xc5y\xa7\xc2\xe0\xb8\xa1\x90N\xed\xe9z0+\x12l\x1c\xdfB\xc8C\r'


dirname = os.path.dirname(__file__)

global combination_data
combination_data = {
  "agriculture": {
    "A1": {
      "corn_area": 200,
      "wheat_area": 125,
      "soybeans_area": 0,
      "sg_area": 125
    },
    "A2": {
      "corn_area": 125,
      "wheat_area": 200,
      "soybeans_area": 200,
      "sg_area": 200
    }
  },
  "energy": {
    "E1": {
      "energy_value": 38,
      "loan_term": 1,
      "interest": 2,
      "num_wind_turbines": 1,
      "nyear_w": 20,
      "capacity_w": 1,
      "cost_w": 1470,
      "degrade_w": 1,
      "wind_factor": 42,
      "num_panel_sets": 3,
      "nyear_s": 25,
      "cost_s": 1750,
      "capacity_s": 250,
      "degrade_s": 0.5,
      "sun_hrs": 5.6,
      "ptc_w": 0,
      "itc_s": 0,
      "ptc_s": 0
    },
    "E2": {
      "energy_value": 50,
      "loan_term": 1,
      "interest": 10,
      "num_wind_turbines": 2,
      "nyear_w": 30,
      "capacity_w": 2,
      "cost_w": 2500,
      "degrade_w": 2,
      "wind_factor": 60,
      "num_panel_sets": 8,
      "nyear_s": 30,
      "cost_s": 4000,
      "capacity_s": 300,
      "degrade_s": 1,
      "sun_hrs": 8,
      "ptc_w": 0.03,
      "itc_s": 30,
      "ptc_s": 0.03
    }
  },
  "irrigation": {
    "W1": {
      "aquifier_level": 200,
      "min_aquifier_level": 30
    },
    "W2": {
      "aquifier_level": 300,
      "min_aquifier_level": 50
    }
  },
  "climate": {
    "C1": {
      "future_processes": "Repeat Historical"
    },
    "C2": {
      "future_processes": "Wetter Future"
    },
    "C3": {
      "future_processes": "Dryer Future"
    },
    "C4": {
      "future_processes": "GCM",
      "climate_model": "RCP4.5"
    },
    "C5": {
      "future_processes": "GCM",
      "climate_model": "RCP8.5"
    }
  }
}

# Homepage EndPoint
@app.route('/')
def index():
    return render_template('homepage.html')

import os

def generate_secret_key():
    return os.urandom(24)

print(generate_secret_key())


# Netlogo Stimulation EndPoint
@app.route('/NetlogoInputV1')
def netlogoinput():
    return render_template('NetlogoInputV1.html')

# Agriculture Page EndPoint
@app.route('/AgricultureV1')
def agriculture():
    return render_template('index.html')

# Water Page EndPoint

@app.route('/WaterV1')
def water():
    return render_template('water.html')

# Energy Page EndPoint

@app.route('/EnergyV1')
def energy():
    return render_template('energy.html')


@app.route('/ChartWindow')
def ChartWindow():
    return render_template('ChartWindow.html')

@app.route('/ClimateV1')
def climate():
    return render_template('climate.html')


@app.route('/AllChartsV1')
def allcharts():
    return render_template('allcharts.html')


@app.route('/download-csv')
def download_csv():
    # Replace the file path with the actual path to your CSV file
    file_path = "data/What NH3 production pays off 2.0.xlsx"
    file_name = "netlogo/Ammonia.xlsx"  # Set the desired file name

    # Serve the file for download
    return send_file(file_path, as_attachment=True, download_name=file_name)



@app.route('/calculateAgriculture', methods=['GET', 'POST'])
def calculate_agriculture():
    key = session.get("key")
    crop_production_img = agriculture_a.crop_production_calculation(key)
    net_calc_img = agriculture_a.net_income_calculation(key)
    result = {
        "crop_production_img": crop_production_img,
        "net_calc_img": net_calc_img
    }
    return jsonify(result)


@app.route('/calculateClimate',methods=['GET', 'POST'])
def calculate_climate():
    key = session.get("key")

    crop_income_img = climate_c.crop_income_calculation(key)

    insur_income_calc_img= climate_c.insurance_income_calculation(key)

    result = {
        "crop_income_img": crop_income_img,
        "insur_income_img": insur_income_calc_img
    }
    return jsonify(result)

@app.route('/calculateEnergy', methods=['GET', 'POST'])
def calculate_energy():
    key = session.get("key")
    farm_energy_production_img_data = energy_e.farm_energy_production_calculation(key)
    energy_net_calc_img_data =  energy_e.energy_net_income_calculation(key)
    result = {
        "farm_energy_production_img_data": farm_energy_production_img_data,
        "energy_net_calc_img_data": energy_net_calc_img_data
    }
    return jsonify(result)

@app.route('/calculateIrrigation', methods=['GET', 'POST'])
def calculate_irrigation():
    key = session.get("key")
    crop_irrigation_img = water_w.crop_groundwater_irrigation(key)
    groundwater_level_img = water_w.groundwater_level(key)

    result = {
        "crop_groundwater_irrigation_data_for_img": crop_irrigation_img,
        "groundwater_level_data_img": groundwater_level_img
    }
    return jsonify(result)

@app.route('/calculate', methods=['GET','POST'])
def calculate():

    data = request.get_json()

    # Agriculture variables
    corn_area = data['agriculture']['corn_area']
    wheat_area = data['agriculture']['wheat_area']
    soybeans_area = data['agriculture']['soybeans_area']
    sg_area = data['agriculture']['sg_area']

    # Energy variables
    energy_value = data['energy']['energy_value']
    loan_term = data['energy']['loan_term']
    interest = data['energy']['interest']
    num_wind_turbines = data['energy']['num_wind_turbines']
    nyear_w = data['energy']['nyear_w']
    capacity_w = data['energy']['capacity_w']
    cost_w = data['energy']['cost_w']
    degrade_w = data['energy']['degrade_w']
    wind_factor = data['energy']['wind_factor']
    num_panel_sets = data['energy']['num_panel_sets']
    nyear_s = data['energy']['nyear_s']
    cost_s = data['energy']['cost_s']
    capacity_s = data['energy']['capacity_s']
    degrade_s = data['energy']['degrade_s']
    sun_hrs = data['energy']['sun_hrs']
    ptc_w = data['energy']['ptc_w']
    itc_s = data['energy']['itc_s']
    ptc_s = data['energy']['ptc_s']

    # Irrigation variables
    aquifier_level = data['irrigation']['aquifier_level']
    min_aquifier_level = data['irrigation']['min_aquifier_level']

    # Number of years variable
    num_of_years = data['numberofyears']['num_of_years']

    # Climate data variable
    future_processes = data['climate']['future_processes']

    # Start year variable
    input_start_of_years = data['StartYear']['input_start_of_years']

    # print(data)
    test_variable = "hi pratik"
    session["combination"] = test_variable    
    
    print("test_variable", test_variable)

    agriculture_data = data.get('agriculture', {})
    energy_data = data.get('energy', {})
    irrigation_data = data.get('irrigation', {})
    climate_data = data.get('climateData', {})

    print(data)
    # print("=====================================")
    # print(combination_data.get("agriculture"))
    # print(combination_data.get("climate"))

    agriculture_key = get_combination.find_matching_key(data, combination_data.get("agriculture") , 'agriculture')
    energy_key = get_combination.find_matching_key(data, combination_data.get("energy"), 'energy', float)
    irrigation_key = get_combination.find_matching_key(data, combination_data.get("irrigation"), 'irrigation')
    climate_key = get_combination.find_matching_key(data, combination_data.get("climate"), 'climate')
    # print(energy_key)
    # print(agriculture_key, energy_key, irrigation_key, climate_key)
    # print(climate_key)
    folder_combination_key = f"{climate_key}{agriculture_key}{energy_key}{irrigation_key}"
    # print(key)

    session["key"] = folder_combination_key

    return jsonify(data)
    
    # combination = find_combination.get_combination(data)
    # if combination:
    #     # Do something with the combination
    #     return jsonify({"combination": combination})
    # else:
    #     return jsonify({"error": "No matching combination found"}), 400

if __name__ == '__main__':
    app.run(debug=True)