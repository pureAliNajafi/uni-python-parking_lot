from datetime import datetime
from Config import config

def calculate_parking(checked_in_date: str, checked_out_date: str, hourly_fee: float ):
    checked_in_date = datetime.strptime(checked_in_date, config.date_format)
    checked_out_date = datetime.strptime(checked_out_date, config.date_format)
    duration = checked_out_date - checked_in_date
    # print(duration,duration.total_seconds())
    hours_parked = duration.total_seconds() / 3600
    total_fee = hours_parked * hourly_fee
    return {"hours_parked":hours_parked, "total_fee":total_fee}

