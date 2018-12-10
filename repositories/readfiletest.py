passport = "A5454549"

with open("./data/customer.txt", "r") as customerfile:
    list_of_lists = []
    for line in customerfile:
        line_list = line.strip().split(",")
        list_of_lists.append(line_list)
    for i in range(len(list_of_lists)-1):
        if list_of_lists[i][1] == passport:
            list_of_lists.remove(list_of_lists[i])
with open("./data/customer.txt", "w") as customerfile:
    for lst in list_of_lists:
        name = lst[0]
        passport = lst[1]
        kredit = lst[2]
        customerfile.write("{},{},{}".format(name, passport, kredit))
        customerfile.write("\n")
            
