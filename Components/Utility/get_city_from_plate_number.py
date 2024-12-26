from Components.File import file
def get_city_from_plate_number(plate_number):
    last_two_digits_of_plate_number=plate_number[-2:]
    plate_city = file.config.codes_city[last_two_digits_of_plate_number]
    return plate_city
# print(get_city_from_plate_number("9812-B-13"))