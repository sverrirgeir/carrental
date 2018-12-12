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
                return 0, 0, 0 

    def write_new_customer(self, new_customer):
        """Writes to customer.txt the data for a new customer"""
        customer_string = new_customer.get_write()
        with open("./data/customer.txt", "a") as customerfile:
            customerfile.write(customer_string)
            customerfile.write("\n")
            return 3

    def print_customer_list(self):
        with open("./data/customer.txt", "r") as customerfile:
            print("\n{:<28}{:^28}{:^28}".format("Nafn", "Vegabréfsnúmer", "Kreditkortanúmer"))
            print("-"*78)
            for line in customerfile:
                line_split = line.split(",")
                name = line_split[0]
                passport = line_split[1]
                kredit = line_split[2]
                print("{:<28}{:^28}{:^28}".format(name, passport, kredit))
            return 
    
    def delete_customer(self, passport):
        with open("./data/customer.txt", "r") as customerfile:
            list_of_lists = []
            for line in customerfile:
                line_list = line.strip().split(",")
                list_of_lists.append(line_list)
            for i in range(len(list_of_lists)):
                if list_of_lists[i][1] == passport:
                    list_of_lists.remove(list_of_lists[i])
        with open("./data/customer.txt", "w") as customerfile:
            for lst in list_of_lists:
                name = lst[0]
                passport = lst[1]
                kredit = lst[2]
                customerfile.write("{},{},{}".format(name, passport, kredit))
                customerfile.write("\n")
            return

    def write_to_file(self, customer, passport, kredit, day1, day2, price, car_type):
        with open("./data/order_confirmation.txt", "w") as f:
            f.write("\n{:^64}".format("Pöntunarstaðfesting"))
            f.write("\n\t================================================================")
            f.write("\n\t{}\t\t\t\t\t{}\t\t\t\t\t{}".format("Nafn","Vegabr.Nr.","Kredit Nr."))
            f.write("\n\t----------------------------------------------------------------")                               