from Models.Order import Order

class OrderRepo:
    def __init__(self):
        pass

    def write_car_order(self, order):
        ''' fallið skrifar inn í orders.txt '''
        order_string = order.get_write()
        with open("./data/orders.txt", "a") as orderfile:
            orderfile.write(order_string)
            orderfile.write("\n")
    
    def print_orders(self):
        ''' fallið prentar út þær pantanir sem eru í orders.txt '''
        with open("./data/orders.txt", "r") as ordersf:
            print("\n\t{:<10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}".format("Vegabréfa N.","Afhendingard.","Skilad.","Verð","Trygging","Fullt Verð","Flokkur"))
            print(" "*8 + "-"*104)
            for line in ordersf:
                linesplit = line.split(",")
                passport = linesplit[0]
                pickupdate = linesplit[1]
                returndate = linesplit[2]
                price = linesplit[3]
                extraprice = linesplit[5]
                fullprice = int(price) + int(extraprice)
                fullprice = int(fullprice)
                fullprice = "{:,}".format(fullprice)
                fullprice = str(fullprice) + " kr"
                extraprice = int(extraprice)
                extraprice = "{:,}".format(extraprice)
                extraprice = str(extraprice) + " kr"
                price = int(price)
                price = "{:,}".format(price)
                price = str(price) + " kr"
                tegund = linesplit[4]
                if tegund == "1":
                    tegund = "Smábíll"
                elif tegund == "2":
                    tegund = "Fólksbíll"
                elif tegund == "3":
                    tegund = "Jeppi"
                else:
                    tegund = "Húsbíll"
                print("\n\t{:<10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}".format(passport, pickupdate, returndate, price, extraprice, fullprice, tegund))
            return
    
    def search_for_orders(self, passport):
        ''' Fallið gerir notanda kleift að leita að ákveðinni pöntunn,
        sé pöntuninn ekki á skrá þá fær notandinn villuskilaboð'''
        with open("./data/orders.txt", "r") as orders:
            list_of_lists = []
            order_list = []
            not_found = 0
            for line in orders:
                line_list = line.strip().split(",")
                list_of_lists.append(line_list)
            for i in range(len(list_of_lists)):
                if list_of_lists[i][0] == passport:
                    list_of_lists[i].insert(0, i)
                    order_list.append(list_of_lists[i])
                    not_found = 1
            if not_found == 1:
                return order_list
            elif not_found == 0:
                return []

    def delete_order(self, order_number):
        ''' Fallið eyðir núverandi pöntun úr orders.txt '''
        with open("./data/orders.txt", "r") as orders:
            list_of_lists = []
            for line in orders:
                line_list = line.strip().split(",")
                list_of_lists.append(line_list)
            list_of_lists.remove(list_of_lists[order_number])
        with open("./data/orders.txt", "w") as orderfile:
            for lst in list_of_lists:
                passport= lst[0]
                day1 = lst[1]
                day2 = lst[2]
                price = lst[3]
                car_type = lst[4]
                insurance = lst[5]
                orderfile.write("{},{},{},{},{},{}".format(passport, day1, day2, price, car_type,insurance))
                orderfile.write("\n")
            return

    def get_order(self, number):
        ''' Fallið les textaskrána orders.txt og finnur ákveðna pöntun út frá pöntunarnúmeri '''
        with open("./data/orders.txt", "r") as orders:
            list_of_lists = []
            for line in orders:
                line_list = line.strip().split(",")
                list_of_lists.append(line_list)
            if number < 0:
                return []
            elif number > len(list_of_lists):
                return []
            return_list = list_of_lists[number]
        return return_list