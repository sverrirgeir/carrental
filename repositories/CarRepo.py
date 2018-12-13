from Models.Car import Car

class CarRepo:

    def __init__(self):
        self.__cars = []


    def print_all_cars(self):
        '''prentar út formataðann lista úr skránni cars.txt með viðeigandi upplýsingum'''
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


    def print_taken_cars(self):
        '''Fallið les in textaskránna cars.txt og prentar út alla þá bíla sem eru í útleig með viðeigandi upplýsingum '''
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
        ''' Fallið prentar út alla þá bíla sem eru lausir til útleigu með viðeigandi upplýsingum'''
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
        '''gerir notanda kleift að leita að bíl sem er skráður í cars.txt og skilar viðeigandi upplýsingum í töflu'''
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
        ''' tekur inn númeraplötu og finnur bílinn sem á að eyða og eyðir honum úr textaskránni cars.txt'''
        with open("./data/cars.txt", "r") as car_string:
            list_of_lists = []
            for line in car_string:
                line_list = line.strip().split(",")
                list_of_lists.append(line_list)
            for i in range(len(list_of_lists)):
                test = list_of_lists[i][2]
                if test == car_plate:
                    list_of_lists.remove(list_of_lists[i])
                    break
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
                    car_string.write("{},{},{},{},{},{},{},{}".format(car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_catagory, car_status))
                    car_string.write("\n")
                return
    
    def write_new_car(self, new_car):
        '''tekur inn upplýsingar um nýjann bíl og skrifar upplýsingarnar inn í textaskránna cars.txt'''
        car_str = new_car.get_write()
        with open("./data/cars.txt", "a") as carfile:
            carfile.write(car_str)
            carfile.write("\n")
            return 2  



    def return_car(self, car_plate):
        '''tekur inn bílnúmer og breytir leigurstöðunni í úr False í True'''
        with open("./data/cars.txt", "r") as car_string:
            list_of_lists = []
            not_found = 0
            for line in car_string:
                line_list = line.strip().split(",")
                list_of_lists.append(line_list)
            for i in range(len(list_of_lists)):
                if list_of_lists[i][2] == car_plate:
                    not_found = 3
                    if list_of_lists[i][7] == "False":
                        list_of_lists[i][7] = "True"
                        with open("./data/cars.txt", "w") as car_string:
                            for lst in list_of_lists:
                                car_model= lst[0]
                                car_year = lst[1]
                                car_plate = lst[2]
                                car_miles = lst[3]
                                car_color = lst[4]
                                car_fuel_type = lst[5]
                                car_status = lst[7]
                                car_catagory = lst[6]
                                car_string.write("{},{},{},{},{},{},{},{}".format(car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_catagory, car_status))
                                car_string.write("\n")
                        return 1
                    else:
                        return 2     
            return not_found

    def rent_car(self, car_plate):
        '''tekur inn bílnúmer ákveðinnar birfreiðar og breytir leigustöðu úr True í False'''
        with open("./data/cars.txt", "r") as car_string:
            list_of_lists = []
            not_found = 0
            for line in car_string:
                line_list = line.strip().split(",")
                list_of_lists.append(line_list)
            for i in range(len(list_of_lists)):
                if list_of_lists[i][2] == car_plate:
                    not_found = 3
                    if list_of_lists[i][7] == "True":
                        list_of_lists[i][7] = "False"
                        with open("./data/cars.txt", "w") as car_string:
                            for lst in list_of_lists:
                                car_model= lst[0]
                                car_year = lst[1]
                                car_plate = lst[2]
                                car_miles = lst[3]
                                car_color = lst[4]
                                car_fuel_type = lst[5]
                                car_status = lst[7]
                                car_catagory = lst[6]
                                car_string.write("{},{},{},{},{},{},{},{}".format(car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_catagory, car_status))
                                car_string.write("\n")
                        return 1
                    else:
                        return 2     
            return not_found

            

