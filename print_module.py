import win32ui

myDoc = ""
with open("./data/order_confirmation.txt", "r") as printf:
        for line in printf:
                mydoc = mydoc + line

myDoc.PrintOut()        