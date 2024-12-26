from Components.File import file
from Components.Gui import gui

#search by name or plate number

parked_vehicles = file.data.checked_in.read_data()
gone_vehicles = file.data.checked_out.read_data()

def search(name_or_plate_input:str):
    results=[]

    for vehicle in parked_vehicles:
        if name_or_plate_input == vehicle["owner_name"] or name_or_plate_input == vehicle["plate_number"] :
            results.append(vehicle)

    for vehicle in gone_vehicles:
        if name_or_plate_input == vehicle["owner_name"] or name_or_plate_input == vehicle["plate_number"] :
            results.append(vehicle)
    return results
