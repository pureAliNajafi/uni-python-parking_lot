from Components.File import file

def get_checked_in_dict_by_plate_number(plate_number: str):
    checked_in_data = file.data.checked_in.read_data()    

    for checked_in_dict in checked_in_data:
        if checked_in_dict["plate_number"] == plate_number:
            return checked_in_dict
    return None
