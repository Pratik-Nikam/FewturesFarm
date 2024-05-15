from flask import Flask, request, jsonify
import os
import pandas as pd
import json
from config import ROOT_DIR

from services import agriculture, climate, energy, water

app = Flask(__name__)

dirname = os.path.dirname(__file__)


@app.route('/calculateAgriculture', methods=['GET', 'POST'])
def calculate_agriculture():
    crop_production_img = agriculture.crop_production_calculation()
    net_calc_img = agriculture.net_income_calculation()
    result = {
        "crop_production_img": crop_production_img,
        "net_calc_img": net_calc_img
    }
    return jsonify(result)

@app.route('/calculateClimate', methods=['GET', 'POST'])
def calculate_climate():
    crop_income_img = climate.crop_income_calculation()
    insurance_income_img = climate.insurance_income_calculation()
    result = {
        "crop_income_img": crop_income_img,
        "insurance_income_img": insurance_income_img
    }
    return jsonify(result)

@app.route('/calculateEnergy', methods=['GET', 'POST'])
def calculate_energy():
    farm_energy_production_img_data = energy.farm_energy_production_calculation()
    energy_net_calc_img_data = energy.energy_net_income_calculation()
    result = {
        "farm_energy_production_img_data": farm_energy_production_img_data,
        "energy_net_calc_img_data": energy_net_calc_img_data
    }
    return jsonify(result)

@app.route('/calculateWater', methods=['GET', 'POST'])
def calculate_water():
    crop_irrigation_img = water.crop_groundwater_irrigation()
    groundwater_level_img = water.groundwater_level()
    result = {
        "crop_irrigation_img": crop_irrigation_img,
        "groundwater_level_img": groundwater_level_img
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)