car_plate = "AUS91"

with open("./data/cars.txt", "r") as car_string:
    list_of_list = []
    not_found = 0
    for line in car_string:
        line_list = line.strip().split(",")
        list_of_list.append(line_list)
    for i in range(len(list_of_list)):
        if list_of_list[i][2] == car_plate:
            not_found = 1
            car_model = list_of_list[i][0]
            car_year = list_of_list[i][1]
            car_plate = list_of_list[i][2]
            car_miles = list_of_list[i][3]
            car_color = list_of_list[i][4]
            car_fuel_type = list_of_list[i][5]
            car_status = list_of_list[i][6]
            car_catagory = list_of_list[i][7]
            print(car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_status, car_catagory)
        else:
            not_found = 0
    if not_found == 0:
        print("not found")