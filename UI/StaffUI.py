from services.CarService import CarService
from services.Order import Order
from services.CustomerService import CustomerService
from services.OrderCar import OrderCar
from Models.Order import Order
from Models.Customer import Customer


class StaffUI():
    def __init__(self):
        self.__cars = CarService()
        self.__customer = CustomerService()
        self.__ordercar = OrderCar()
        
        
        
    def main_menu(self):
        """Prints out the main menu and returns a input sentence asking for a choice"""
        choice1 = "1. Pantanir"
        choice2 = "2. Viðskiptavinir"
        choice3 = "3. Bílar"
        choice4 = "4. Verðlisti"
        choice5 = "5. Panta bíl"
        choice6 = "6. Skila bíl"
        choice7 = "7. Hætta"
        print("\n\t{:^10}".format("Bílaleiga ehf"))
        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4, choice5, choice6, choice7))
        
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
        
        elif choice == "6":
            pass
            
        elif choice == '7':
            print("\tLoka forriti...")
            return

        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.main_menu()

    def print_order_menu(self):
        """Prentar út valmöguleika fyrir pantanir og biður um val og leiðir notenda á rétta staði"""
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
            passport = input("\n\tVegabréfsnúmer: ").upper()
            nr_list = self.search_for_order(passport)
            self.customer_order_menu(nr_list)
        elif choice == '3':
            self.__ordercar.print_list_of_orders()
        elif choice == '4':
            self.main_menu()
        else:
            print("Vitlaust val, vinsamlegast veldu aftur")
            self.print_order_menu()
    
    def search_for_order(self, passport):
        list_of_orders = self.__ordercar.search_for_orders(passport)
        
        print("\n\t{:<10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}".format("nr.","Vegabréfa N.","Afhendingard.","Skilad.","Verð","Flokkur"))
        print(" "*8 + "-"*88)
        nr_list = []
        for lst in list_of_orders:
            nr = lst[0]
            nr_list.append(nr)
            passport = lst[1]
            day1 = lst[2]
            day2 = lst[3]
            price = lst[4]
            price = "{:,}".format(int(price))
            type_of_car = lst[5]
            print("\n\t{:<10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}".format(nr, passport,day1,day2,price,type_of_car))
        return nr_list
    

    def print_clients_menu(self):
        choice1 = "1. Fletta upp Viðskiptavin"
        choice2 = "2. Skrá nýjan viðskiptavin"
        choice3 = "3. Listi af Viðskiptavinum"
        choice4 = "4. Til baka"

        print("\n\t{:^10}".format("Viðskiptavinir"))
        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3,choice4))
        choice = input("\n\tValmöguleiki: ")

        if choice == '1':
            #sendir notenda í viðeigandi fall
            self.search_customer()

        elif choice == "2":
            #sendir notenda í viðeigandi fall
            self.add_new_customer()

        elif choice == '3':
            #sendir notenda í viðeigandi fall
            self.__customer.print_customer_list()

            #valmöguleiki til þess að fara til baka eftir að listi hefur verið prentaður
            print("\n\t1. Til baka")
            choice = input("\n\tValmöguleiki: ")
            if choice == "1":
                self.print_clients_menu()
            else:
                self.print_clients_menu()

        elif choice == '4':
            self.main_menu()
        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.print_clients_menu()
    
    def add_new_customer(self):
        #Input from the user about the new customer
        first_name = input("\tFornafn(og millinafn): ").strip()
        last_name = input("\tEftirnafn: ").strip()
        passport = input("\tVegabréfsnúmer: ").upper().strip()
        kredit = input("\tKreditkortanúmer(engin bandstrik): ").strip()
        #upplýsingar sendar í models klasann customer
        new_customer = Customer(first_name, last_name, passport, kredit)
        #kallað í add_customer fallið í customerservice
        customer = self.__customer.add_customer(new_customer)
        #hér er kannað hvað fallið skilar, og þá er farið yfir hvort allt var rétt innslegið
        if customer == 1:
            print("\n\tEkki rétt Vegabréfsnúmer! \n\treyndu aftur\n")
            self.print_clients_menu()
            return
        elif customer == 2:
            print("\n\tEkki rétt kreditkortanúmer! \n\treyndu aftur\n")
            self.print_clients_menu()
            return
        elif customer == 3:
            print("\n\tViðskiptavinur hefur verið skráður!\n")
            self.main_menu()



    def search_customer(self):
        #prentar út fundið viðskiptavin
        choice1 = "1. Skoða pantanir"
        choice2 = "2. Breyta upplýsingum"
        choice3 = "3. Afskrá viðskiptavin"
        choice4 = "4. Til baka"
        
        line = "-"*80
        passport = input("\n\tVegabréfsnúmer: ").upper()
        customer, passport, kredit = self.__customer.find_customer(passport)
        if customer == 0:
            print("\n\tEngin viðskiptavinur er skráður á þetta númer!!")
            self.print_clients_menu()
            return
        if customer == 1:
            print("\n\tEkki rétt skráð inn! \n\tVegabréfsnúmer á að vera 8 letur á lengd")
            self.print_clients_menu()
            return

        print("")
        print("\t{:<27}{:^27}{:^27}".format("Nafn", "Vegabréfsnúmer", "Kreditkortanúmer"))
        print("\t" + line)
        print("\t{:<27} {:^27} {:^27}".format(customer, passport, kredit))

        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4))
        choice = input("\n\tValmöguleiki: ")

        if choice == '1':
            nr_list = self.search_for_order(passport)
            self.customer_order_menu(nr_list)
        elif choice == '2':
            #Þurfum að skoða þetta betur
            self.__customer.delete_customer(passport)
            self.add_new_customer()
        elif choice == '3':
            #fer inn í fall sem yfirskrifar textafile með nýjum textafile án viðskiptavinarins
            self.__customer.delete_customer(passport)
            print("\n\tViðskiptavin hefur verið eytt úr kerfinu!")
            self.print_clients_menu()
        elif choice == '4':
            self.print_clients_menu()
    
    def customer_order_menu(self, nr_list):
        choice1 = "1. Breyta pöntun"
        choice2 = "2. Eyða pöntun"
        choice3 = "3. Prenta pöntunarstaðfestingu"
        choice4 = "4. Til baka"

        print("\n\t{:^10}".format("Pöntun"))
        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4))
        choice = input("\n\tValmöguleiki: ")

        if choice == "1":
            number = int(input("\n\tHvaða pöntun viltu breyta?"))
            self.__ordercar.delete_order(number)
            print("\n\tskráðu pöntun með nýjum upplýsingum!")
            self.print_order_car_menu()
        elif choice == "2":
            number = int(input("\n\tHvaða pöntun viltu eyða?: "))
            self.__ordercar.delete_order(number)
            print("\n\tPöntun hefur verið eytt!")
            self.main_menu()
        elif choice == "3":
            self.print_order_confirmation()
        elif choice == "4":
            self.print_order_menu()
        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.customer_order_menu(nr_list)


    def print_order_confirmation(self):
        print("Sent í prentara...")


    def print_car_menu(self):
        """Prints out the cars menu and returns a input sentence asking for a choice"""
        choice1 = "1. Listi yfir Bílaflota"
        choice2 = "2. Bílar í Útleigu"
        choice3 = "3. Lausir Bílar"
        choice4 = "4. Fletta upp Bíl"
        choice5 = "5. Skrá nýjan bíl"
        choice6 = "6. Til baka"
        print("\n\t{:^10}".format("Bílaleiga ehf"))
        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4, choice5, choice6))

        choice = input("\n\tValmöguleiki: ")

        if choice == '1':
            self.__cars.print_cars()
            self.print_car_menu()
        elif choice == '2':
            self.__cars.print_taken()
            self.print_car_menu()
        elif choice == '3':
            self.__cars.print_available()
            self.print_car_menu()
        elif choice == '4':
            self.search_car()
        elif choice == '5':
            self.__cars.add_car()          
        elif choice == '6':
            self.main_menu()
        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.print_car_menu()    



    def search_car(self):

        line ="-"*72
        car_plate = input("\n\tNúmer bifreiðar: ").upper()
        car_model, car_year, car_plate, car_miles, car_color, car_fuel_type, car_status, car_catagory= self.__cars.find_cars(car_plate)
       
        if car_model == 0:
            print("\n\tEnginn bíll er skráður með þetta númer!")
            self.print_car_menu()
            return
        if car_model == 1:
            print("\n\tEkki rétt skráð inn! \n\tBílnúmer á að vera 5 letur á lengd")
            self.print_car_menu()
            return
        print("")
        print("\n\t{:>4}{:>15}{:>8}{:>9}{:>7}{:>10}{:>6}{:>9}".format("Tegund", "Árgerð", "Númer", "Keyrsla", "Litur", "Eldsneyti", "Staða", "Flokkur"))
        print("\t" + line)
        print("\t{:<10}\t{:^}\t{:^}\t{:^}\t{:^}\t{:^}\t{:^}\t{:^}".format(car_model.capitalize(), car_year, car_plate, car_miles, car_color.capitalize(), car_fuel_type, car_status, car_catagory))

        #Prentar út valmyndi fyrir leit af bílum
        choice1 = "1. Afskrá bíl"
        choice2 = "2. Setja á lista yfir lausar bifreiðar"
        choice3 = "3. Skrá í útleigu"
        choice4 = "4. Til baka"

        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4))
        choice = input("\n\tValmöguleiki: ")
        if choice == "1":
            self.__cars.delete_cars(car_plate)
            print("\n\tBíl hefur verið eytt úr kerfinu!")
            self.print_car_menu()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            self.main_menu()                 
        
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
        """Prentar út pöntunarskjá fyrir pöntun"""
        choice1 = "1. skrá pöntun"
        choice2 = "2. Til baka"

        print("\n\t{:^10}".format("Pantanir"))
        print("\n\t{:<30}\n\t{:<10}\n".format(choice1, choice2))

        choice = input("\n\tValmöguleiki: ")
        
        if choice == "1":
            passport = input("\n\tVegabréfsnúmer: ").upper()
            #sækir find customer fallið og skila gildum sem notuð eru til að geyma gögn
            customer, passport, kredit = self.__customer.find_customer(passport)

            if customer == 0:
                print("\n\tEngin viðskiptavinur er skráður á þetta númer!\n")
                self.add_new_customer()
                return
            if customer == 1:
                print("\n\tEkki rétt skráð inn! \n\tVegabréfsnúmer á að vera 8 letur á lengd")
                self.print_order_car_menu()
                return
            fullprice,today,someday,carchoice = self.__ordercar.order_price()
            print("\n\t\tHeildarverð: {:,}".format(fullprice))
            new_order = Order(passport, today, someday, fullprice, carchoice)
            self.__ordercar.get_car_order(new_order)
            print("\n\tPöntun hefur verið skráð!")
            self.main_menu()

        elif choice == "2":
            self.print_order_menu()
        else:
            print("\nVitlaust val, vinsamlegast veldu aftur!")
            self.print_order_car_menu()

    
