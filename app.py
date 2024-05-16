from flask import Flask, render_template, request, jsonify, send_file
import os
import pandas as pd
import json

from config import ROOT_DIR

from services import climate_c, energy_e, water_w, agriculture_a, find_combination

app = Flask(__name__, template_folder='template')

dirname = os.path.dirname(__file__)

# Homepage EndPoint
@app.route('/')
def index():
    return render_template('homepage.html')

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
    crop_production_img = agriculture_a.crop_production_calculation()
    net_calc_img = agriculture_a.net_income_calculation()
    result = {
        "crop_production_img": crop_production_img,
        "net_calc_img": net_calc_img
    }
    return jsonify(result)

@app.route('/calculateClimate', methods=['GET', 'POST'])
def calculate_climate():
    crop_income_img = climate_c.crop_income_calculation()
    insurance_income_img = climate_c.insurance_income_calculation()
    result = {
        "crop_income_img": crop_income_img,
        "insurance_income_img": insurance_income_img
    }
    return jsonify(result)

@app.route('/calculateEnergy', methods=['GET', 'POST'])
def calculate_energy():
    farm_energy_production_img_data = energy_e.farm_energy_production_calculation()
    energy_net_calc_img_data =  energy_e.energy_net_income_calculation()
    result = {
        "farm_energy_production_img_data": farm_energy_production_img_data,
        "energy_net_calc_img_data": energy_net_calc_img_data
    }
    return jsonify(result)

@app.route('/calculateWater', methods=['GET', 'POST'])
def calculate_water():
    crop_irrigation_img = water_w.crop_groundwater_irrigation()
    groundwater_level_img = water_w.groundwater_level()
    result = {
        "crop_irrigation_img": crop_irrigation_img,
        "groundwater_level_img": groundwater_level_img
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
    future_processes = data['ClimateData']['future_processes']

    # Start year variable
    input_start_of_years = data['StartYear']['input_start_of_years']
    print(data)
    return jsonify(data)
    
    # combination = find_combination.get_combination(data)
    # if combination:
    #     # Do something with the combination
    #     return jsonify({"combination": combination})
    # else:
    #     return jsonify({"error": "No matching combination found"}), 400

if __name__ == '__main__':
    app.run(debug=True)