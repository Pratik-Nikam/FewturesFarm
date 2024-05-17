def find_matching_key(data_dict, ref_dict, data_key, value_converter=str):
    for key, values in ref_dict.items():
        match = True
        for k, v in values.items():
            data_value = data_dict.get(data_key, {}).get(k, '')
            if value_converter(data_value) != value_converter(v):
                match = False
                break
        if match:
            return key
    return None
