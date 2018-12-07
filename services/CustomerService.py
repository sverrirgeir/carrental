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
            
