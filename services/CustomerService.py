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
        if len(kredit) == 16:
            if type(kredit) = int:
                return True
        else:
            return False
    
    def add_customer(self, new_customer):
        if self.valid_kredit_number(new_customer.get_kredit()):
            if self.valid_number(new_customer.get_passport()):
                self.__customer.write_new_customer(new_customer)
                return 3
            else:
                return 1
        else:
            return 2
            
