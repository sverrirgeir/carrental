from services.CarService import CarService
from services.CustomerService import CustomerService
from services.OrderCar import OrderCar
from Models.Order import Order
from Models.Customer import Customer
from Models.Car import Car
from repositories.PrintRepo import PrintRepo
import os


class StaffUI():
    def __init__(self):
        self.__cars = CarService()
        self.__customer = CustomerService()
        self.__ordercar = OrderCar()
        self.__printrepo = PrintRepo()
        
        
    def main_menu(self):
        """Prentar út "main menu" og biður um val, skilar notanda á réttann stað"""
        choice1 = "1. Pantanir"
        choice2 = "2. Viðskiptavinir"
        choice3 = "3. Bílar"
        choice4 = "4. Verðlisti"
        choice5 = "5. Panta bíl"
        choice6 = "6. Skila bíl"
        choice7 = "7. Skrá út bíl"
        choice8 = "8. Hætta"

        print("\n\t{:^10}".format("Bílaleiga ehf"))
        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8))
        
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
            self.return_car()  

        elif choice == '7':
            self.rent_car()

        elif choice == '8':
            print("\tLoka forriti...")
            return
        else:
            print("\n\tVitlaust val, vinsamlegast veldu aftur!")
            self.main_menu()

    def return_car(self):
        """prentar út lista yfir upptekna bíla og biður um bílnúmer á bíl
        sem skil á og skráir hann sem skilaðann"""
        self.__cars.print_taken()
        car_plate = input("\n\tBílnúmer bíls sem skila á('q' til að hætta við): ").upper()
        if car_plate == "Q":
            return self.main_menu()
        result = self.__cars.return_car(car_plate)
        if result == 0:
            print("\n\tBíll er ekki á skrá, vinsamlegast reyndu aftur")
            self.return_car()
        elif result == 3:
            print("\n\tBílnúmer ekki rétt slegið inn")
            self.return_car()
        return self.main_menu()

    def rent_car(self):
        """prentar út lista yfir lausa bíla og biður um bílnúmer á bíl
        sem leigja á og skráir hann sem uppteknann"""
        self.__cars.print_available()
        car_plate = input("\n\tBílnúmer bíls sem leigja á('q' til að hætta við): ").upper()
        if car_plate == "Q":
            return self.main_menu()
        result = self.__cars.rent_car(car_plate)
        if result == 0:
            print("\n\tBíll er ekki á skrá, vinsamlegast reyndu aftur")
            self.rent_car()
        elif result == 3:
            print("\n\tBílnúmer ekki rétt slegið inn")
            self.rent_car()
        return self.main_menu()

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
            #biður um input frá notenda um vegabréfsnúmer og skilar lista yfir allar pantanir á því númeri
            passport = input("\n\tVegabréfsnúmer: ").upper()
            nr_list = self.search_for_order(passport)
            if nr_list == []:
                print("\tEngin pöntun fannst á þessu vegabréfsnúmeri!")
                self.print_order_menu()
            else:
                self.customer_order_menu(nr_list)
        elif choice == '3':
            #prentar út lista yfir allar pantanir
            self.__ordercar.print_list_of_orders()
            self.print_order_menu()
        elif choice == '4':
            self.main_menu()
        else:
            print("Vitlaust val, vinsamlegast veldu aftur")
            self.print_order_menu()
    
    def search_for_order(self, passport):
        """Fall sem tekur inn vegabréfsnúmer og prentar töflu af öllum pöntunum á því númeri"""
        #sækja lista af listum af þeim pöntunum sem eru á þessu númeri
        list_of_orders = self.__ordercar.search_for_orders(passport)
        if list_of_orders == 0:
            print("\n\tEkki rétt Vegabréfsnúmer! \n\treyndu aftur\n")
            return self.main_menu()
        #prenta út listann í format töflu formi
        print("\n\t{:<10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}".format("nr.","Vegabréfa N.","Afhendingard.","Skilad.","Heildarverð","Flokkur"))
        print(" "*8 + "-"*88)
        nr_list = []
        for lst in list_of_orders:
            nr = lst[0]
            nr_list.append(nr)
            passport = lst[1]
            day1 = lst[2]
            day2 = lst[3]
            price = lst[4]
            type_of_car = lst[5]
            insurance = lst[6]
            fullprice = int(price) + int(insurance)
            fullprice = "{:,}".format(fullprice)
            print("\n\t{:<10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}".format(nr, passport,day1,day2,fullprice,type_of_car))
        return nr_list
    

    def print_clients_menu(self):
        """fall sem prentar út valmöguleika í viðskiptavina menu og skilar notanda á rétta staði"""
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
            print("\n\tVitlaust val, vinsamlegast veldu aftur!")
            self.print_clients_menu()
    
    def add_new_customer(self):
        """fall sem tekur inn upplýsingar frá notanda um nýjann viðskiptavin
        og sem síðan sendir upplýsingarnar áfram til að verða skráðar í textaskrána customer.txt"""
        #Input frá notenda um kúnnan
        first_name = input("\n\tFornafn(og millinafn): ").strip()
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
        """fall sem prentar út viðskiptavin út frá vegabréfsnúmeri og 
        gefur notenda valmöguleiga um aðgerðir tengdar þeim viðskiptavin"""
        choice1 = "1. Skoða pantanir"
        choice2 = "2. Breyta upplýsingum"
        choice3 = "3. Afskrá viðskiptavin"
        choice4 = "4. Til baka"
        
        line = "-"*80
        #beðið um vegabréfsnúmer frá notenda
        passport = input("\n\tVegabréfsnúmer: ").upper()
        #fall sem skilar upplýsingum um þennan ákveðna notenda
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
            #finnur allar pantanir sem þessi ákveðni viðskiptavinur á og sendir í viðeigandi fall
            nr_list = self.search_for_order(passport)
            self.customer_order_menu(nr_list)
        elif choice == '2':
            #Fall til að breyta uppls. um viðskiptavin, byrjar a því að eyða honum og biður svo notenda um
            #að skrá nýjar upplýsingar um notenda

            #eyðir notenda
            self.__customer.delete_customer(passport)
            print("\n\tVinsamlegast skráðu inn nýjar upplýsingar!\n")
            #skráir hann upp á nýtt
            self.add_new_customer()
        elif choice == '3':
            #Sendir uppls. í fall sem eyðir viðskiptavin
            self.__customer.delete_customer(passport)
            print("\n\tViðskiptavin hefur verið eytt úr kerfinu!")
            self.print_clients_menu()
        elif choice == '4':
            self.print_clients_menu()
    
    def customer_order_menu(self, nr_list):
        """fall sem prentar út valmöguleika fyrir pantanir ákveðins viðskiptavins"""
        choice1 = "1. Breyta pöntun"
        choice2 = "2. Eyða pöntun"
        choice3 = "3. Prenta pöntunarstaðfestingu"
        choice4 = "4. Til baka"

        print("\n\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4))
        choice = input("\n\tValmöguleiki: ")

        if choice == "1":
            #biður um pöntun sem notandi breyta og eyðir henni og biður notenda um uppfærðar uppls.
            number = input("\n\tHvaða pöntun viltu breyta?: ")
            if number.isdigit():
                number = int(number)
                result = self.__ordercar.delete_order(number)
                if result == 1:
                    print("\n\tPöntunarnúmer er ekki til")
                    return self.customer_order_menu(nr_list)
            else:
                print("\n\tVitlaust val, vinsamlegast veldu aftur!")
                self.customer_order_menu(nr_list)

            print("\n\tskráðu pöntun með nýjum upplýsingum!")
            self.print_order_car_menu()
        elif choice == "2":
            #biður um pöntunarnúmer frá notenda og eyðir þeirri ákveðnu pöntun
            number = input("\n\tHvaða pöntun viltu eyða?: ")
            if number.isdigit():
                number = int(number)
                result = self.__ordercar.delete_order(number)
                if result == 1:
                    print("\n\tPöntunarnúmer er ekki til")
                    return self.customer_order_menu(nr_list)
                print("\n\tPöntun hefur verið eytt!")
                self.main_menu()
            else:
                print("\n\tVitlaust val, vinsamlegast veldu aftur!")
                self.customer_order_menu(nr_list)
        elif choice == "3":
            #skrifar pöntunarstaðfestingu og prentar á skjáinn
            self.print_order_confirmation()
        elif choice == "4":
            self.print_order_menu()
        else:
            print("\n\tVitlaust val, vinsamlegast veldu aftur!")
            self.customer_order_menu(nr_list)


    def print_order_confirmation(self):
        '''Prentar út upplýsingar um pöntun út frá pöntunarnúmeri'''
        #biður um pöntunarnúmer sem notandi vill fá staðfestingu á
        number = input("\n\tPöntunarnúmer: ")
        if number.isdigit():
            number = int(number)
            #sækir pöntunarlista notenda
            order_list = self.__ordercar.get_order(number)
            if order_list == []:
                print("\n\tPöntun ekki á lista!")
                self.print_order_confirmation()
            passport = order_list[0]
            day1 = order_list[1]
            day2 = order_list[2]
            price = order_list[3]
            car_type = order_list[4]
            insurance = order_list[5]
            full_price = int(insurance)+ int(price)
            full_price = "{:,}".format(full_price)
            #sækir upplýsingar um viðskiptavin
            customer, passport, kredit = self.__customer.find_customer(passport)
            self.__customer.write_to_file(customer, passport, kredit, day1, day2, price, car_type)

            print("\n{:^64}".format("Pöntunarstaðfesting"))
            print("\n========================================================================")
            print("\n\t{:<10}\t{:^10}\t{:^10}".format("Nafn","Vegabr.Nr.","Kredit Nr."))
            print("\n------------------------------------------------------------------------")
            print("\n\t{:<10}\t{:^10}\t{:^10}".format(customer,passport,kredit))
            print("\n------------------------------------------------------------------------")
            print("\n\t{:<10}\t{:^10}\t{:^10}\t{:^10}".format("Frá","Til","Verð","Flokkur"))
            print("\n------------------------------------------------------------------------")
            print("\n\t{:<10}\t{:^10}\t{:^10}\t{:^10}".format(day1,day2,full_price,car_type))
            print("\n========================================================================")
            print("\n\t{:<30}".format("1. Til baka"))
            choice = input("\n\tValmöguleiki: ")
        

            if choice == "1":
                self.main_menu()
            else:
                print("\n\tVitlaust val, vinsamlegast veldu aftur!")
                self.main_menu()
        else:
            print("\n\tVitlaust val, vinsamlegast veldu aftur!")
            self.print_order_confirmation()




    def print_car_menu(self):
        """Prentar út valmynd fyrir bíla og biður um input frá notenda um hvað hann vill gera"""
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
            self.add_new_car()          
        elif choice == '6':
            self.main_menu()
        else:
            print("\n\tVitlaust val, vinsamlegast veldu aftur!")
            self.print_car_menu()    



    def search_car(self):
        """Leitar af ákveðinni bifreið út frá bílnúmeri og prentar upplýsingar á skjáinn"""
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

        #Prentar út valmyndi fyrir þennan ákvðna bíl
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
            self.__cars.return_car(car_plate)
            self.print_car_menu()            
        elif choice == "3":
            self.__cars.rent_car(car_plate)
            self.print_car_menu()
        elif choice == "4":
            self.main_menu()                 
        
    def print_price_list(self):
        """Fallið prentar út verðlista fyrir bílaleigubíla"""
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
        print("\n\t{:<10}\t{:^10}\t{:^10}".format("Flokkur","Daggjald","Trygging"))
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
        print("\n\t{:<30}".format("1. Til baka"))
        choice = input("\n\tValmöguleiki: ")

        if choice == "1":
            self.main_menu()
        else:
            print("\n\tVitlaust val, vinsamlegast veldu aftur!")
            self.print_price_list()

    def print_order_car_menu(self):
        """Prentar út pöntunarskjá fyrir pöntun"""
    
        passport = input("\n\tVegabréfsnúmer: ").upper()
        #sækir find customer fallið og skila gildum sem notuð eru til að geyma gögn
        customer, passport, kredit = self.__customer.find_customer(passport)

        if customer == 0:
            print("\n\tEngin viðskiptavinur er skráður á þetta númer!\n")
            print("\t1. Nýskrá viðskiptavin")
            print("\t2. Slá inn nýtt vegabréfsnúmer")
            choice = input("\n\tValmöguleiki: ")
            if choice == "1":
                self.add_new_customer()
            elif choice == "2":
                self.print_order_car_menu()
            else:
                self.print_order_car_menu()
            
        if customer == 1:
            print("\n\tEkki rétt skráð inn! \n\tVegabréfsnúmer á að vera 8 letur á lengd")
            self.print_order_menu()
            return
        fullprice,today,someday,carchoice,extraprice = self.__ordercar.order_price()
        if today == 0:
            self.print_order_car_menu()
        print("\n\t\tHeildarverð: {:,}".format(fullprice + extraprice))
        new_order = Order(passport, today, someday, fullprice, carchoice, extraprice)
        fullprice = int(fullprice)
        if fullprice < 10000:
            print("\n\tDagsetning skrifuð vitlaus inn: ")
            self.print_order_car_menu()
        else:
            self.__ordercar.get_car_order(new_order)
            print("\n\tPöntun hefur verið skráð!")

        self.__printrepo.send_email(customer,today,someday)
        self.main_menu()

    

    def add_new_car(self):
        ''' búa til user interface þar sem notandinn getur skráð inn nýjan bíl '''
        ''' ef bílnúmer er skráð inn vitlaust þarf að láta notandann vita '''
        model = input("\n\ttegund bíls: ").strip().capitalize()
        year = input("\tÁrgerð(YYYY): ").strip()
        plate = input("\tBílnúmer: ").strip().upper()
        miles = input("\tKeyrsla bíls (í km): ").strip()
        color = input("\tLitur bíls: ").strip().capitalize()
        fuel_type = input("\tEldsneytis tegund(Bensín eða Dísel): ").strip()
        print("\n\t1. Smábíll\n\t2. Fólksbíll\n\t3. Jeppi\n\t4. Húsbíll")
        category = input("\tflokkur: ").strip()
        status = True
        new_car = Car(model, year, plate, miles, color, fuel_type, category, status) 
        decision = self.__cars.add_car(new_car)
        if decision == 2:
            print("\n\tBíl hefur verið bætt á skrá")
            self.print_car_menu()
        elif decision == 1:
            print("\n\tVitlaust skráð inn bílnúmer")
            self.print_car_menu()
    
    #def print_doc(self, filename):
        """fall sem prentar út í prentara textaskrá sem sett er inn"""
        """ATH virkar en vantar module win32 í tölvuna svo við commentuðum þetta út"""
        #myWord = Dispatch('Word.Application')
        #myWord.Visible = 1

        #myDoc = myWord.Documents.Add()
        #myRange = myDoc.Range(0,1)
        #with open(filename, "r") as printf:
            #for line in printf:
                #myRange.InsertAfter(line)

        #myDoc.PrintOut()
