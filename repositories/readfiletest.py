
passport = "A3056435"

with open("./data/customer.txt", "r") as customerfile:
            for line in customerfile:
                line_list = line.split(",")
                if line_list[1] == passport:
                    name = line_list[0]
                    passport = line_list[1]
                    kredit = line_list[2]
                    print("\t{}\t{}".format(name, passport))
                    
                else:
                    pass