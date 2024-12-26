PATH="Config/cities_list.txt"

def read_city_codes(location):
    cities = {}
    with open(location, 'r') as file:
        for line in file:
            parts = line.strip().split('-')
            plate_numbers = parts[0].split(',')
            city = parts[1]
            for plate_number in plate_numbers:
                cities.__setitem__(f"{plate_number}",city)
    return cities

codes_city = read_city_codes(PATH)
