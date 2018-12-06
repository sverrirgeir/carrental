
from services.OrderCar import OrderCar

class OrderCarUI():
    def __init__(self):
        self.OrderCar = OrderCar()
    
    def print_order_car_menu():
        choice1 = "1. Núverandi Viðskiptavinir"
        choice2 = "2. Nýr Viðskiptavinur"
        choice3 = "3. Til baka"

        print("")
        print("\t{:^10}".format("Pantanir"))
        print("")
        print("\t{:<30}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3))
        print("")
        return input("\tValmöguleiki: ")

