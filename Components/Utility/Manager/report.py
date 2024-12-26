from datetime import datetime, timedelta
import copy
from Components.File import file
from Components.Gui import gui
from Config import config

checked_in_vehicles = file.data.checked_in.read_data()
checked_out_vehicles=file.data.checked_out.read_data()
def past_week_parked_vehicles():
    #filter_and_sort_past_week_parked_vehicles
    parked_vehicles=copy.deepcopy(checked_in_vehicles)
    today = datetime.now()
    seven_days_ago = today - timedelta(days=7)

    filtered_and_formatted = []
    for pv in parked_vehicles:
        # Parse the date from the string
        check_in_date = datetime.strptime(pv["checked_in_date"], config.date_format)

        # Filter entries from the past 7 days
        if check_in_date >= seven_days_ago:
            if check_in_date.date() == today.date():
                # Replace the date with "Today [time]"
                pv["checked_in_date"] = f"Today {check_in_date.strftime('%H:%M:%S')}"
            else:
                # Format as the original
                pv["checked_in_date"] = check_in_date.strftime(config.date_format)
            filtered_and_formatted.append(pv)

    # Sort the filtered list by date
    filtered_and_formatted.sort(
        key=lambda x: datetime.strptime(x["checked_in_date"], config.date_format) if "Today" not in x["checked_in_date"] else datetime.strptime(f"{today.date()} {x['checked_in_date'].split()[-1]}", config.date_format),
        reverse=True
    )
    gui.list("Vehicles parked since the past week (sorted by date)",filtered_and_formatted)

def even_and_odd_plates():
    results={
        "even_plates":[],
        "odd_plates":[]
    }
    parked_vehicles=copy.deepcopy(checked_in_vehicles)
    for pv in parked_vehicles:
        if int(pv["plate_number"][-4]) %2 == 0:
            results["even_plates"].append(pv)
        else:
            results["odd_plates"].append(pv)
    # GUI
    gui.print("Vehicles grouped by odd and even plate numbers:")    
    gui.list("Even plates",results["even_plates"])
    gui.list("Odd plates",results["odd_plates"])


def vehicle_details_by_type():
    group_vehicles_by_key("vehicle_type")

def vehicle_details_by_city():
    group_vehicles_by_key("plate_city")
   
def group_vehicles_by_key(key:str):
    results = []
    parked_vehicles = copy.deepcopy(checked_in_vehicles)

    for pv in parked_vehicles:
        if pv[key] not in [r[key] for r in results]:
            results.append({key:pv[key],"count":1,"vehicles":[pv]})
        else:
            for r in results:
                if r[key] == pv[key]:
                    r["vehicles"].append(pv)
                    r["count"]+=1

    # GUI
    for r in results:
        gui.print(f"{key.replace("_"," ")}:", r[key], f"({r['count']})")
        gui.list("Vehicles", r["vehicles"])

def past_week_income():
    #filter_and_sort_past_week_parked_vehicles
    parked_vehicles=copy.deepcopy(checked_out_vehicles)
    today = datetime.now()
    seven_days_ago = today - timedelta(days=7)

    result={"income":0.0,"vehicles":[]}
    for pv in parked_vehicles:
        # Parse the date from the string
        checked_out_date = datetime.strptime(pv["checked_in_date"], config.date_format)

        # Filter entries from the past 7 days
        if checked_out_date >= seven_days_ago:
            result["income"] += pv["total_fee"]
            result["vehicles"].append(pv) 

    gui.print("Income from the past week and related vehicles")
    gui.list(f"Income:{result["income"]}",result["vehicles"])




"""def vehicle_details_by_type():
    results=[] #[{"vehicle_type":"","vehicles":[]}]

    parked_vehicles=copy.deepcopy(checked_in_vehicles)
    for pv in parked_vehicles:
        if pv["vehicle_type"] not in [r["vehicle_type"] for r in results]:
            results.append({"vehicle_type":pv["vehicle_type"],"count":1,"vehicles":[pv]})
        else:
            for r in results:
                if r["vehicle_type"] == pv["vehicle_type"]:
                    r["vehicles"].append(pv)
                    r["count"]+=1

    # gui
    for r in results:
        gui.print("vehicle type:",r["vehicle_type"],f"({r["count"]})")
        gui.list("vehicles",r["vehicles"])

    return results
        
def vehicle_details_by_city():
    pvs=[{'owner_name': 'test', 'plate_number': 'test-30', 'plate_city': 'Tehran', 'vehicle_type': 'Bicycle', 'brand_and_model': 'ttt-333', 'hourly_fee': 1.0, 'checked_in_date': '2024-12-23 05:57:45'}, {'owner_name': 'ali', 'plate_number': 'thn-20', 'plate_city': 'Tehran', 'vehicle_type': 'Luxury Vehicle', 'brand_and_model': 'bmw-ix', 'hourly_fee': 30.0, 'checked_in_date': '2024-10-24 02:40:21'}, {'owner_name': 'reza', 'plate_number': 'ixu-13', 'plate_city': 'Isfahan', 'vehicle_type': 'Car', 'brand_and_model': 'bmw-s1', 'hourly_fee': 5.0, 'checked_in_date': '2024-12-24 15:01:33'}, {'owner_name': 'Amir', 'plate_number': 'wes-30', 'plate_city': 'Tehran', 'vehicle_type': 'Car', 'brand_and_model': 'iran_khodro-samanf', 'hourly_fee': 5.0, 'checked_in_date': '2024-12-24 15:55:43'}]

    results=[] 

    for pv in pvs:
        if pv["plate_city"] not in [r["plate_city"] for r in results]:
            results.append({"plate_city":pv["plate_city"],"count":1,"vehicles":[pv]})
        else:
            for r in results:
                if r["plate_city"] == pv["plate_city"]:
                    r["vehicles"].append(pv)
                    r["count"]+=1

    # gui
    for r in results:
        gui.print("vehicle city:",r["plate_city"],f"({r["count"]})")
        gui.list("vehicles",r["vehicles"])

    return results
    
     
"""