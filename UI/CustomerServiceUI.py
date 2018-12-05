from services.CustomerService import CustomerService

class CustomerServiceUI():
    def __init__(self):
        self.__customerservice = CustomerService()

    def print_clients_menu(self):
        choice1 = "1. Fletta upp Viðskiptavin"
        choice2 = "2. Listi af Viðskiptavinum"
        choice3 ="3. Til baka"
  

        print("")
        print("\t{:^10}".format("Viðskiptavinir"))
        print("")
        print("\t{:<30}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3,))
        print("")
        return input("\tValmöguleiki: ")