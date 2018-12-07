from Models.Customer import Customer

class CustomerRepo:
    def __init__(self):
        self.__customer = ""
    
    def find_customer(self, passport):
        with open("./data/customer.txt", "r") as customerfile:
            list_of_lists = []
            not_found = 0
            for line in customerfile:
                line_list = line.strip().split(",")
                list_of_lists.append(line_list)
            for i in range(len(list_of_lists)):
                if list_of_lists[i][1] == passport:
                    not_found = 1
                    name = list_of_lists[i][0]
                    passport = list_of_lists[i][1]
                    kredit = list_of_lists[i][2]
                    return name, passport, kredit
                else:
                    not_found = 0
            if not_found == 0:
                return "Not found", "Not found", "Not found"

                                             