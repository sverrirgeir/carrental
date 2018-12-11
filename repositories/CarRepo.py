from Models.Car import Car

class CarRepo:

    def __init__(self):
        self.__cars = []


    def print_all_cars(self):
        with open("./data/cars.txt", "r") as car_string:
                print("\n{:>4}{:>15}{:>8}{:>9}{:>7}{:>10}{:>6}{:>9}".format("Tegund", "Árgerð", "Númer", "Keyrsla", "Litur", "Eldsneyti", "Staða", "Flokkur"))
                print("-"*73)
                for line in car_string:
                    car_list = line.split(",")
                    car_model = car_list[0]
                    car_year = car_list[1]
                    car_plate = car_list[2]
                    car_miles = car_list[3]
                    car_color = car_list[4]
                    car_fuel_type = car_list[5]
                    car_catagory = car_list[6]
                    car_status = car_list[7].strip()

                    if car_status == "True":
                        car_status = "Laus"
                    elif car_status == "False":
                        car_status = "Tekinn"

                    if car_catagory == '1':
                        car_catagory = "Smábíll"
                    elif car_catagory == '2':
                        car_catagory = "Fólksbíll"
                    elif car_catagory == '3':
                        car_catagory = "Jeppi"
                    else:
                        car_catagory = "Húsbíll"

                    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(car_model.capitalize(), car_year, car_plate, car_miles, car_color.capitalize(), car_fuel_type, car_status, car_catagory))
                    #return car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_catagory, car_status

    # def print_all_cars(self):
    #     with open("./data/cars.txt", "r") as car_string:
    #         car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_catagory, car_status = self.list_of_cars()
    #         for line in car_string:
    #             print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(car_model.capitalize(), car_year, car_plate, car_miles, car_color.capitalize(), car_fuel_type, car_status, car_catagory))

    def print_taken_cars(self):
        with open("./data/cars.txt", "r") as car_string:
                print("\n{:>4}{:>15}{:>8}{:>9}{:>7}{:>10}{:>6}{:>9}".format("Tegund", "Árgerð", "Númer", "Keyrsla", "Litur", "Eldsneyti", "Staða", "Flokkur"))
                print("-"*73)
                for line in car_string:
                    car_list = line.split(",")
                    car_model = car_list[0]
                    car_year = car_list[1]
                    car_plate = car_list[2]
                    car_miles = car_list[3]
                    car_color = car_list[4]
                    car_fuel_type = car_list[5]
                    car_catagory = car_list[6]
                    car_status = car_list[7].strip()

                    if car_catagory == '1':
                        car_catagory = "Smábíll"
                    elif car_catagory == '2':
                        car_catagory = "Fólksbíll"
                    elif car_catagory == '3':
                        car_catagory = "Jeppi"
                    elif car_catagory == '4':
                        car_catagory = "Húsbíll"

                    if car_status == "True":
                        car_status = "Laus"
                    elif car_status == "False":
                        car_status = "Tekinn"
                        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(car_model.capitalize(), car_year, car_plate, car_miles, car_color.capitalize(), car_fuel_type, car_status, car_catagory))

    def print_available_cars(self):
        with open("./data/cars.txt", "r") as car_string:
                print("\n{:>4}{:>15}{:>8}{:>9}{:>7}{:>10}{:>6}{:>9}".format("Tegund", "Árgerð", "Númer", "Keyrsla", "Litur", "Eldsneyti", "Staða", "Flokkur"))
                print("-"*73)
                for line in car_string:
                    car_list = line.split(",")
                    car_model = car_list[0]
                    car_year = car_list[1]
                    car_plate = car_list[2]
                    car_miles = car_list[3]
                    car_color = car_list[4]
                    car_fuel_type = car_list[5]
                    car_catagory = car_list[6]
                    car_status = car_list[7].strip()

                    if car_catagory == '1':
                        car_catagory = "Smábíll"
                    elif car_catagory == '2':
                        car_catagory = "Fólksbíll"
                    elif car_catagory == '3':
                        car_catagory = "Jeppi"
                    elif car_catagory == '4':
                        car_catagory = "Húsbíll"

                    if car_status == "True":
                        car_status = "Laus"
                        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(car_model.capitalize(), car_year, car_plate, car_miles, car_color.capitalize(), car_fuel_type, car_status, car_catagory))
                    elif car_status == "False":
                        car_status = "Tekinn"


    def find_car(self, car_plate):
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
                    car_status = list_of_list[i][7]
                    car_catagory = list_of_list[i][6]

                    if car_status == "True":
                        car_status = "Laus"
                    else:
                        car_status = "Tekinn"
                    
                    if car_catagory == '1':
                        car_catagory = "Smábíll"
                    elif car_catagory == '2':
                        car_catagory = "Fólksbíll"
                    elif car_catagory == '3':
                        car_catagory = "Jeppi"
                    elif car_catagory == '4':
                        car_catagory = "Húsbíll"
                    

                    return car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_status, car_catagory
                else:
                    not_found = 0
            if not_found == 0:
                return 0,0,0,0,0,0,0,0       

    def delete_cars(self, car_plate):
        with open("./data/cars.txt", "r") as car_string:
            list_of_lists = []
            for line in car_string:
                line_list = line.strip().split(",")
                list_of_lists.append(line_list)
            for i in range(len(list_of_lists)):
                if list_of_lists[2] == car_plate:
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
                return
    
    def write_new_car(self, new_car):
        '''skrifar nýjan bíl inn í textaskránna cars.txt'''
        car_str = new_car.get_write()
        with open("./data/cars.txt", "a") as carfile:
            carfile.write(car_str)
            carfile.write("\n")
            return 2
          