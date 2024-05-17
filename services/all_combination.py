

def find_matching_key(data, agriculture_values):
    for key, values in agriculture_values.items():
        match = True
        for k, v in values.items():
            if str(v) != data['agriculture'].get(k):
                match = False
                break
        if match:
            return key
    return None

data = {'agriculture': {'corn_area': '200', 'wheat_area': '125', 'soybeans_area': '0', 'sg_area': '125'}}

agriculture_values = {
    "A1": {"corn_area": 200, "wheat_area": 125, "soybeans_area": 0, "sg_area": 125},
    "A2": {"corn_area": 125, "wheat_area": 200, "soybeans_area": 200, "sg_area": 200}
}

matching_key = find_matching_key(data, agriculture_values)

if matching_key:
    print(f"The matching key is: {matching_key}")
else:
    print("No matching key found.")
    
    



def find_matching_key(data, energy_values):
    for key, values in energy_values.items():
        match = True
        for k, v in values.items():
            if float(data['energy'].get(k, '')) != v:
                match = False
                break
        if match:
            return key
    return None

energy_data = {'energy': {'energy_value': '38.0', 'loan_term': '1.0', 'interest': '2.0', 'num_wind_turbines': '1',
                          'nyear_w': '20', 'capacity_w': '1', 'cost_w': '1470', 'degrade_w': '1.0', 'wind_factor': '42',
                          'num_panel_sets': '3', 'nyear_s': '25', 'cost_s': '1750', 'capacity_s': '250',
                          'degrade_s': '0.5', 'sun_hrs': '5.6', 'ptc_w': '0.000', 'itc_s': '0', 'ptc_s': '0.000'}}

energy_values = {
    "E1": {
        "energy_value": 38.0, "loan_term": 1.0, "interest": 2.0, "num_wind_turbines": 1, "nyear_w": 20,
        "capacity_w": 1, "cost_w": 1470, "degrade_w": 1.0, "wind_factor": 42, "num_panel_sets": 3,
        "nyear_s": 25, "cost_s": 1750, "capacity_s": 250, "degrade_s": 0.5, "sun_hrs": 5.6,
        "ptc_w": 0.000, "itc_s": 0, "ptc_s": 0.000
    },
    "E2": {
        "energy_value": 50.0, "loan_term": 1.0, "interest": 10.0, "num_wind_turbines": 2, "nyear_w": 30,
        "capacity_w": 2, "cost_w": 2500, "degrade_w": 2.0, "wind_factor": 60, "num_panel_sets": 8,
        "nyear_s": 30, "cost_s": 4000, "capacity_s": 300, "degrade_s": 1.0, "sun_hrs": 8.0,
        "ptc_w": 0.03, "itc_s": 30, "ptc_s": 0.03
    }
}

matching_key = find_matching_key(energy_data, energy_values)

if matching_key:
    print(f"The matching key is: {matching_key}")
else:
    print("No matching key found.")
    
    
    
def find_matching_key(data, irrigation_values):
    for key, values in irrigation_values.items():
        match = True
        for k, v in values.items():
            if str(data['irrigation'].get(k, '')) != str(v):
                match = False
                break
        if match:
            return key
    return None

irrigation_data = {'irrigation': {'aquifier_level': '200', 'min_aquifier_level': '30'}}

irrigation_values = {
    "W1": {"aquifier_level": 200, "min_aquifier_level": 30},
    "W2": {"aquifier_level": 300, "min_aquifier_level": 30}
}

matching_key = find_matching_key(irrigation_data, irrigation_values)

if matching_key:
    print(f"The matching key is: {matching_key}")
else:
    print("No matching key found.")
    
    


def find_matching_key(data, climate_values):
    for key, values in climate_values.items():
        match = True
        for k, v in values.items():
            if str(data['climate_data'].get(k, '')) != str(v):
                match = False
                break
        if match:
            return key
    return None

climate_data = {'climate_data': {'future_processes': 'GCM', 'climate_model': 'RCP4.5'}}

climate_values = {
    "C1": {"future_processes": "Repeat Historical"},
    "C2": {"future_processes": "Wetter Future"},
    "C3": {"future_processes": "Dryer Future"},
    "C4": {"future_processes": "GCM", "climate_model": "RCP4.5"},
    "C5": {"future_processes": "GCM", "climate_model": "RCP8.5"}
}

matching_key = find_matching_key(climate_data, climate_values)

if matching_key:
    print(f"The matching key is: {matching_key}")
else:
    print("No matching key found.")