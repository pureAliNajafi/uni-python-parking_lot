import datetime
from Components.Gui import gui
from Components.Utility import utility
from Components.File import file
from Config import config

def check_out():

# get date
    checked_out_date=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
# prompt name 
    owner_name = gui.input("Name?")

# prompt plate's number
    plate_number = gui.input("Plate number?")

    related_checked_in_dict = utility.get_checked_in_dict_by_plate_number(plate_number) 

# authenticate
    def authenticate():
        return owner_name == related_checked_in_dict["owner_name"]
    
    if not authenticate():
        print("Warning Error! Authentication failed.")
        return

# get parking related data (hourly fee, total fee)
    parking_info = utility.calculate_parking(related_checked_in_dict["checked_in_date"],
                                             checked_out_date,
                                             related_checked_in_dict["hourly_fee"])
    
    gui.input(f"You're total fee will bee {parking_info["total_fee"]} ,press Enter to continue")
    

# 
    new_check_out_row  = {
    **related_checked_in_dict,  # Spread the existing key-value pairs
    "check_out_date": checked_out_date,  # Add new key with default value
    **parking_info  # Add another new key with default value
    }

# handle data files
    file.data.checked_in.delete_row(plate_number)
    file.data.checked_out.add_row(new_check_out_row)

    file.receipts.new_receipt(new_check_out_row)

