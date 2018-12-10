from Models.Car import Car

class CarRepo:

    def __init__(self):
        self.__cars = []

    def list_of_cars(self):
        car_string=open("./data/cars.txt","r")
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

                    #print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(car_model.capitalize(), car_year, car_plate, car_miles, car_color.capitalize(), car_fuel_type, car_status, car_catagory))
            return car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_catagory, car_status, car_list

    def print_all_cars(self):
        car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_catagory, car_status, car_list = self.list_of_cars()
        for line in car_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(car_model.capitalize(), car_year, car_plate, car_miles, car_color.capitalize(), car_fuel_type, car_status, car_catagory))
