from Components.File import file
def get_vehicle_type_dict_by_id(id:str):
    vehicle_dict=file.config.vehicles_fees[int(id)-1]  
    return vehicle_dict