car_plate = "ZF222"

if len(car_plate) == 5:
    if car_plate[0:3].isalpha():
        if car_plate[3:].isnumeric():
            print("True")
else:
    print("False")