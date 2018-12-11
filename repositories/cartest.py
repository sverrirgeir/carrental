car_plate = "DAS75"

  

with open("./data/cars.txt", "r") as car_string:
    list_of_lists = []
    for line in car_string:
        line_list = line.strip().split(",")
        list_of_lists.append(line_list)
    for i in range(len(list_of_lists)):
        test = list_of_lists[i][2]
        if test == car_plate:
            list_of_lists.remove(list_of_lists[i])
with open("./data/cars.txt", "w") as car_string:
    for lst in list_of_lists:
        car_model= lst[0]
        car_year = lst[1]
        car_plate = lst[2]
        car_miles = lst[3]
        car_color = lst[4]
        car_fuel_type = lst[5]
        car_status = lst[6]
        car_catagory = lst[7]
        car_string.write("{},{},{},{},{},{},{},{}".format(car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_status, car_catagory))
        car_string.write("\n")
        