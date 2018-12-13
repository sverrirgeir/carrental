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
        if self.valid_plate(car_plate):
            return self.__car.find_car(car_plate)
        else:
            return 1,1,1,1,1,1,1,1

    def valid_plate(self, car_plate):
        """Athugar hvort bílnúmer sé gilt, kannar hvort það séu 5 að lengd"""
        if len(car_plate) == 5:
            return True
        else:
            return False

    def delete_cars(self, car_plate):
        """tekur inn rétt bílnúmer"""
        return self.__car.delete_cars(car_plate)
     
    def add_car(self,new_car):
        '''Ef númerplatan er gild þá er bílnum bætt við'''
        '''Ef ekki þá fær notandinn villu skilaboð'''
        if self.valid_plate(new_car.get_plate()):
            self.__car.write_new_car(new_car)
            return 2
        else:
            return 1

    def return_car(self, car_plate):
        """kallar í fallið return_car í carrepo með bílnúmeri
        Prentar einnig út villuboð"""
        if self.valid_plate(car_plate):
            result = self.__car.return_car(car_plate)
        else:
            return 3
        if result == 1:
            print("\n\tBíll hefur verið skráður sem laus")
        elif result == 2:
            print("\n\tBíll er núþegar á skrá yfir lausar bifreiðar")
        return result

    def rent_car(self, car_plate):
        """Kallar í fallið rent_car í carrepo með bílnúmeri"""
        if self.valid_plate(car_plate):
            result = self.__car.rent_car(car_plate)
        else:
            return 3
        if result == 1:
            print("\n\tBíll hefur verið skráður í leigu")
            return result
        elif result == 2:
            print("\n\tBíll er núþegar á skrá yfir leigðar bifreiðar")
            return result
        return result


            
