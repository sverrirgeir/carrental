from UI.OrderUI import OrderUI
from UI.CarsUI import CarsUI

class StaffUI:
    def __init__(self):
        self.__order_ui = OrderUI()
        self.__cars_ui = CarsUI()

    def main_menu(self):
        """Prints out the main menu and returns a input sentence asking for a choice"""
        choice1 = "1. Pantanir"
        choice2 = "2. Viðskiptavinir"
        choice3 = "3. Bílar"
        choice4 = "4. Verðlisti"
        choice5 = "5. Panta bíl"
        choice6 = "6. Hætta"
        print("")
        print("\t{:^10}".format("Bílaleiga ehf"))
        print("")
        print("\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4, choice5, choice6))
        print("")
        
        choice = input("\tValmöguleiki: ")

        if choice == '1':
            self.__order_ui.print_order_menu()

        elif choice == '2':
            pass

        elif choice == '3':
            self.__cars_ui.print_car_menu()
        
        elif choice == '4':
            pass

        elif choice == '5':
            pass

        elif choice == '6':
            return

        else:
            print("Please input valid choice")
            self.main_menu()
