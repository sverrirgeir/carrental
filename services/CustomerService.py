from repositories.CustomerRepo import CustomerRepo

class CustomerService:
    def __init__(self):
        self.__customer = CustomerRepo()

    def find_customer(self, passport):
        """Sendir vegabréfsnúmer í fallið find_customer í customerepo eftir að
        vegabréfsnúmerið hefur verið athugað"""
        if self.valid_number(passport):
            return self.__customer.find_customer(passport)
        else:
            return 1, 1, 1
            
    def valid_number(self, passport):
        """Athugar hvort vegabréfsnúmer sé rétt eða 8 stafir af lengd"""
        if len(passport) == 8:
            return True
        else:
            return False

    def valid_kredit_number(self, kredit):
        """athugar hvort kreditkortanúmer sé í lagi eða 16 tölustafir"""
        try:
            int(kredit)
        except ValueError:
            return False
        if len(kredit) != 16:
            return False
        else: 
            return True

    
    def add_customer(self, new_customer):
        """tekur tinn stak af customer klasanum og skilar honum eftir
        að kreditkortanúmer og vegabréfsnúmer hefur verið "validatað" """
        #fyrst kannað hvort kreditkortanúmerið sé rétt slegið inn
        if self.valid_kredit_number(new_customer.get_kredit()):
            #kannað hvort vegabréfsnúmer sé rétt
            if self.valid_number(new_customer.get_passport()):
                #haldið áfram í write_new_customer í customerepo og viðskiptavin bætt í textaskrá
                self.__customer.write_new_customer(new_customer)
                return 3
            else:
                return 1
        else:
            return 2
    
    def print_customer_list(self):
        """Kallar í fallið print_customer_list"""
        return self.__customer.print_customer_list()

    def delete_customer(self, passport):
        """Tekur inn vegabréfsnúmer sem búið er að tjékka"""
        return self.__customer.delete_customer(passport)

    def write_to_file(self, customer, passport, kredit, day1, day2, price, car_type):
        """tekur inn breytur um pöntun og kúnna og skilar þeim í customerrepo order_confirmation"""
        return self.__customer.write_to_file(customer, passport, kredit, day1, day2, price, car_type)

            
