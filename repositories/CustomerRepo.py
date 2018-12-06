from Models.Customer import Customer

class CustomerRepo:
    def __init__(self):
        self.__customer = ""
    
    def find_customer(self, passport):
        with open("./data/customer.txt", "r") as customerfile:
            for line in customerfile:
                line_list = line.split(",")
                if line_list[1] == passport:
                    name = line_list[0]
                    passport = line_list[1]
                    kredit = line_list[2]
                    return "\t{:<18}\t{:>18}".format(name, passport)

                                             