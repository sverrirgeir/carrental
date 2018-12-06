from services.CarService import CarService
from services.Order import Order
from services.CustomerService import CustomerService

class StaffUI():
    def __init__(self):
        self.__cars = CarService()
        self.__order = Order()
        self.__customer = CustomerService()
        
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
            self.print_order_menu()

        elif choice == '2':
            self.print_clients_menu()

        elif choice == '3':
            self.print_car_menu()
        
        elif choice == '4':
            self.print_price_list()

        elif choice == '5':
            self.print_order_car_menu()
            
        elif choice == '6':
            print("\tLoka forriti...")
            return

        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.main_menu()

    def print_order_menu(self):
        
        choice1 = "1. Skrá nýja pöntun"
        choice2 = "2. Leita af pöntun"
        choice3 ="3. Pöntunarlisti"
        choice4 ="4. Til baka"

        print("")
        print("\t{:^10}".format("Pantanir"))
        print("")
        print("\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4))
        print("")
        choice = input("\tValmöguleiki: ")

        if choice == '1':
            self.print_order_car_menu()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            self.main_menu()
        else:
            print("Vitlaust val, vinsamlegast veldu aftur")
            self.print_order_menu()
    
    def print_clients_menu(self):
        choice1 = "1. Fletta upp Viðskiptavin"
        choice2 = "2. Listi af Viðskiptavinum"
        choice3 ="3. Til baka"
  
        print("")
        print("\t{:^10}".format("Viðskiptavinir"))
        print("")
        print("\t{:<30}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3,))
        print("")
        choice = input("\tValmöguleiki: ")

        if choice == '1':
            self.search_customer()
        elif choice == '2':
            pass
        elif choice == '3':
            self.main_menu()
        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.print_clients_menu()

    def search_customer(self):
        #prentar út fundið viðskiptavin
        choice1 = "1. Skoða pantanir"
        choice2 = "2. Breyta upplýsingum"
        choice3 = "3. Afskrá viðskiptavin"
        choice4 = "4. Til baka"
        
        line = "-"*43
        passport = input("\n\tVegabréfsnúmer: ")
        customer = self.__customer.find_customer(passport)
        print("")
        print("\t{:<18}\t{:>18}".format("Nafn", "Vegabréfsnúmer"))
        print("\t" + line)
        print(customer)

        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4))
        choice = input("\n\tValmöguleiki: ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            self.print_clients_menu()



    def print_car_menu(self):
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

        choice = input("\tValmöguleiki: ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            self.main_menu()
        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.print_car_menu()
        
    def print_price_list(self):
        insurance = "Aukatrygging 30.000 kr."
        choice1 = "Smábílar"
        price1 = "10.000 kr."
        choice2 = "Fólksbílar"
        price2 = "15.000 kr."
        choice3 = "Jeppar"
        price3 = "20.000 kr."
        choice4 = "Húsbílar"
        price4 = "25.000 kr."
        over100 = "Athugið dagverð miðast við 100 ekna km á dag að meðaltali yfir \n leigutíma. Gjald fyrir akstur umfram 100 km miðast við 1% \n af dagverði fyrir hvern kílómetra umfram 100km."
        print("")
        print("{:^64}".format("Verðlisti"))
        print("")
        print("================================================================")
        print("")
        print("\t{:<10}\t{:^10}\t{:^10}".format("Flokkur","Verð","Trygging"))
        print("")
        print("----------------------------------------------------------------")
        print("")
        print("\t{:<10}\t{:^10}\t{:^10}".format(choice1,price1,insurance))
        print("")
        print("----------------------------------------------------------------")
        print("")
        print("\t{:<10}\t{:^10}\t{:^10}".format(choice2,price2,insurance))
        print("")
        print("----------------------------------------------------------------")
        print("")
        print("\t{:<10}\t{:^10}\t{:^10}".format(choice3,price3,insurance))
        print("")
        print("----------------------------------------------------------------")
        print("")
        print("\t{:<10}\t{:^10}\t{:^10}".format(choice4,price4,insurance))
        print("")
        print("----------------------------------------------------------------")
        print("")
        print(over100)
        print("")
        print("================================================================")
        print("")
        print("\t{:<30}\n\t{:<10}".format("1. Prenta út Verðlista","2. Til baka"))
        print("")
        choice = input("\tValmöguleiki: ")

        if choice == "1":
            pass
        elif choice == "2":
            self.main_menu()
        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.print_price_list()

    def print_order_car_menu(self):
        choice1 = "1. Núverandi Viðskiptavinir"
        choice2 = "2. Nýr Viðskiptavinur"
        choice3 = "3. Til baka"

        print("")
        print("\t{:^10}".format("Pantanir"))
        print("")
        print("\t{:<30}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3))
        print("")
        choice = input("\tValmöguleiki: ")
        
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            self.print_order_menu()
        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.print_order_car_menu()

