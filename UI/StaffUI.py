from services.CarService import CarService
from services.Order import Order
from services.CustomerService import CustomerService
from services.OrderCar import OrderCar

class StaffUI():
    def __init__(self):
        self.__cars = CarService()
        self.__order = Order()
        self.__customer = CustomerService()
        self.__ordercar = OrderCar()
        
        
    def main_menu(self):
        """Prints out the main menu and returns a input sentence asking for a choice"""
        choice1 = "1. Pantanir"
        choice2 = "2. Viðskiptavinir"
        choice3 = "3. Bílar"
        choice4 = "4. Verðlisti"
        choice5 = "5. Panta bíl"
        choice6 = "6. Hætta"
        print("\n\t{:^10}".format("Bílaleiga ehf"))
        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4, choice5, choice6))
        
        choice = input("\n\tValmöguleiki: ")

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
        choice3 = "3. Pöntunarlisti"
        choice4 = "4. Til baka"

        print("\n\t{:^10}".format("Pantanir"))
        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4))

        choice = input("\n\tValmöguleiki: ")

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
        choice2 = "2. Skrá nýjan viðskiptavin"
        choice3 = "3. Listi af Viðskiptavinum"
        choice4 = "4. Til baka"
  
        print("\n\t{:^10}".format("Viðskiptavinir"))
        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3,choice4))
        choice = input("\n\tValmöguleiki: ")

        if choice == '1':
            self.search_customer()
        elif choice == "2":
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            self.main_menu()
        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.print_clients_menu()

    def search_customer(self):
        #prentar út fundið viðskiptavin
        #ATHATHATH virkar ekki ef slegið er inn vitlaust fyrst og svo rétt skil ekki alveg
        choice1 = "1. Skoða pantanir"
        choice2 = "2. Breyta upplýsingum"
        choice3 = "3. Afskrá viðskiptavin"
        choice4 = "4. Til baka"
        
        line = "-"*80
        passport = input("\n\tVegabréfsnúmer: ").upper()
        customer, passport, kredit = self.__customer.find_customer(passport)
        print("")
        print("\t{:<27}{:^27}{:^27}".format("Nafn", "Vegabréfsnúmer", "Kreditkortanúmer"))
        print("\t" + line)
        print("\t{:<27} {:^27} {:^27}".format(customer, passport, kredit))

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
        print("\n\t{:^10}".format("Bílaleiga ehf"))
        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4, choice5,))

        choice = input("\n\tValmöguleiki: ")

        if choice == '1':
            self.__cars.print_cars()
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
        print("\n{:^64}".format("Verðlisti"))
        print("\n================================================================")
        print("\n\t{:<10}\t{:^10}\t{:^10}".format("Flokkur","Verð","Trygging"))
        print("\n----------------------------------------------------------------")
        print("\n\t{:<10}\t{:^10}\t{:^10}".format(choice1,price1,insurance))
        print("\n----------------------------------------------------------------")
        print("\n\t{:<10}\t{:^10}\t{:^10}".format(choice2,price2,insurance))
        print("\n----------------------------------------------------------------")
        print("\n\t{:<10}\t{:^10}\t{:^10}".format(choice3,price3,insurance))
        print("\n----------------------------------------------------------------")
        print("\n\t{:<10}\t{:^10}\t{:^10}".format(choice4,price4,insurance))
        print("\n----------------------------------------------------------------")
        print("\n{}".format(over100))
        print("\n================================================================")
        print("\n\t{:<30}\n\t{:<10}".format("1. Prenta út Verðlista","2. Til baka"))
        choice = input("\n\tValmöguleiki: ")

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

        print("\n\t{:^10}".format("Pantanir"))
        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3))

        choice = input("\n\tValmöguleiki: ")
        
        if choice == "1":
            passport = input("\n\tVegabréfsnúmer: ").upper()
            customer, passport, kredit = self.__customer.find_customer(passport)
            fullprice = self.__ordercar.order_price()
            print("\n\t\tHeildarverð:", fullprice)

            
            print("\n\t\tHeildarverð:", fullprice)
        elif choice == "2":
            pass
        elif choice == "3":
            self.print_order_menu()
        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.print_order_car_menu()
