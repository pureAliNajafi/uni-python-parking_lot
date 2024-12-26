from Components.File.Data.common_funcs import read_data as read_data_func
from Components.File.Data.common_funcs import add_row as add_row_func
from Components.File.Data.common_funcs import delete_row as delete_row_func

FILE="checked_in"

def read_data():
    return read_data_func(FILE)

def add_row(new_row):
    add_row_func(FILE,new_row)

def delete_row(plate_number):
    delete_row_func(FILE,plate_number)

