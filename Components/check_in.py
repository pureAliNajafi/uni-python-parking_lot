import datetime
from Components.Gui import gui
from Components.Utility import utility
from Components.File import file
from Config import config

def check_in():

# if len( checked_in_vehicles ) > file.cap ->Print(We are out of free space) ,else rest of the code

    if  len(file.data.checked_in.read_data()) == config.capacity :
         gui.print("We are full, you cant park here")
         return
# get date
    checked_in_date=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# prompt name 
    owner_name = gui.input("Name?")
    gui.print(f"welcome {owner_name}")

# prompt plate's number --then--> get city
    plate_number = gui.input("Plate number?")
    plate_city = utility.get_city_from_plate_number(plate_number)
    gui.print(f"I see you're from {plate_city}, Nice!")

# prompt vehicle's type --then--> get substract hourly fee
    gui.list("Select you're vehicle's type",file.config.vehicles_fees,["Hourly Fee"],index=False)
    vehicle_id=gui.input("You're vehicle type ?")
    related_vehicle_type_dict=utility.get_vehicle_type_dict_by_id(vehicle_id)
    vehicle_type=related_vehicle_type_dict["Vehicle"]
    hourly_fee=related_vehicle_type_dict["Hourly Fee"]
    gui.print(f"The {vehicle_type}'s hourly fee is {hourly_fee}")

# prompt brand_and_model
    brand_and_model = gui.input("Please enter your car's brand and model, separated by a dash (e.g., Toyota-Corolla)")

    new_check_in_row = {
    "owner_name": owner_name,
    "plate_number": plate_number,
    "plate_city": plate_city,
    "vehicle_type": vehicle_type,
    "brand_and_model": brand_and_model,
    "hourly_fee": hourly_fee,
    "checked_in_date": checked_in_date,
    }
    file.data.checked_in.add_row(new_check_in_row)

