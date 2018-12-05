from services.carservice import carservice

class CarsUI:
    def __init__(self):
        self.__cars = CarService()

def print_car_menu():
    """Prints out the cars menu and returns a input sentence asking for a choice"""
    choice1 = "1. Listi yfir Bílaflota"
    choice2 = "2. Bílar í Útleigu"
    choice3 = "3. Fletta upp Bíl"
    choice4 = "4. Lausir Bílar"
    choice5 = "5. Til baka"
    print("")
    print("\t{:^10}".format("Bílaleiga ehf"))
    print("")
    print("\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4, choice5,))
    print("")
    return input("\tValmöguleiki: ")