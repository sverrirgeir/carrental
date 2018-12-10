from repositories.CustomerRepo import CustomerRepo

class CustomerService:
    def __init__(self):
        self.__customer = CustomerRepo()

    def find_customer(self, passport):
        """sends a valid passport number into customerrepo to find the customer"""
        if self.valid_number(passport):
            return self.__customer.find_customer(passport)
        else:
            return 1, 1, 1
            
    def valid_number(self, passport):
        """checks if the passport number is valid"""
        if len(passport) == 8:
            return True
        else:
            return False

    def valid_kredit_number(self, kredit):
        """checks if the kredit card number is valid"""
        try:
            int(kredit)
        except ValueError:
            return False
        if len(kredit) != 16:
            return False
        else: 
            return True

    
    def add_customer(self, new_customer):
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
        return self.__customer.print_customer_list()

    def delete_customer(self, passport):
        """takes in a validated passport number"""
        return self.__customer.delete_customer(passport)
            
