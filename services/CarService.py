from repositories.CarRepo import CarRepo

class CarService:
    
    def __init__(self):
        self.__car = CarRepo()

    def print_cars(self):
       return self.__car.print_all_cars()
    
    