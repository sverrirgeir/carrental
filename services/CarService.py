from repositories.CarRepo import CarRepo

class CarService:
    
    def __init__(self):
        self.__car = CarRepo()

    def print_cars(self):
        return self.__car.print_all_cars()

    def print_taken(self):
        return self.__car.print_taken_cars()

    def print_available(self):
        return self.__car.print_available_cars()
    
    
    def find_cars(self, car_plate):
        """finnur virkt bílnúmer og skilar inn í CarRepo"""
        if self.valid_number(car_plate):
            return self.__car.find_car(car_plate)
        else:
            return 1,1,1,1,1,1,1,1

    def valid_number(self, car_plate):
        """Athugar hvort bílnúmer sé gilt"""
        if len(car_plate) == 5:
            return True
        else:
            return False


    def delete_cars(self, car_plate):
        """tekur inn rétt bílnúmer"""
        return self.__car.delete_cars(car_plate)
            
