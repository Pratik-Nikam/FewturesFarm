def get_combination(data):
    agriculture_values = {
        "A1": {"Corn Area": 200, "Wheat Area": 125, "Soybeans Area": 0, "SG Area": 125},
        "A2": {"Corn Area": 125, "Wheat Area": 200, "Soybeans Area": 200, "SG Area": 200}
    }
    energy_values = {
        "E1": {
            "energy_value": 38, "loan_term": 1, "interest": 2, "num_wind_turbines": 1, "nyear_w": 20,
            "capacity_w": 1, "cost_w": 1470, "degrade_w": 1, "wind_factor": 42, "num_panel_sets": 3,
            "nyear_s": 25, "cost_s": 1750, "capacity_s": 250, "degrade_s": 0.5, "sun_hrs": 5.6,
            "ptc_w": 0, "itc_s": 0, "ptc_s": 0
        },
        "E2": {
            "energy_value": 50, "loan_term": 1, "interest": 10, "num_wind_turbines": 2, "nyear_w": 30,
            "capacity_w": 2, "cost_w": 2500, "degrade_w": 2, "wind_factor": 60, "num_panel_sets": 8,
            "nyear_s": 30, "cost_s": 4000, "capacity_s": 300, "degrade_s": 1, "sun_hrs": 8,
            "ptc_w": 0.03, "itc_s": 30, "ptc_s": 0.03
        }
    }
    water_values = {
        "W1": {"Aquifer Level": 200, "Min. Aquifer Level": 30},
        "W2": {"Aquifer Level": 300, "Min. Aquifer Level": 50}
    }
    climate_values = {
        "C1": {"Future Processes": "Repeat Historical"},
        "C2": {"Future Processes": "Wetter Future"},
        "C3": {"Future Processes": "Dryer Future"},
        "C4": {"Future Processes": "GCM", "Climate Model": "RCP4.5"},
        "C5": {"Future Processes": "GCM", "Climate Model": "RCP8.5"}
    }

    # Determine agriculture combination
    agriculture_combo = next((key for key, value in agriculture_values.items() if value == data['agriculture']), None)

    # Determine energy combination
    energy_combo = next((key for key, value in energy_values.items() if value == data['energy']), None)

    # Determine water combination
    water_combo = next((key for key, value in water_values.items() if value == data['irrigation']), None)

    # Determine climate combination
    climate_combo = next((key for key, value in climate_values.items() if value == data['ClimateData']), None)

    if agriculture_combo and energy_combo and water_combo and climate_combo:
        combination = f"{climate_combo}{agriculture_combo}{energy_combo}{water_combo}"
        return combination
    else:
        return None
