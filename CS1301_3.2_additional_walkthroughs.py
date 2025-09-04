#additional_conditionals_problem_1.py
#This program determines if a car rental can be approved based on the car's location, the requested location, and any associated fees.
car_location = "airport"
requested_location = "home"
parking_fee = True
moving_fee = True

if car_location == requested_location:
    if car_location == "airport":
        if parking_fee == True:
            print("rental approved")
        else:
            print("rental denied - parking fee")
    else:
        print("rental approved")
else:
    if moving_fee == True:
        if requested_location == "airport":
            if parking_fee == True:
                print("rental approved")
            else:
                print("rental denied - parking fee")
        else:
            print("rental approved")
    else:
        print("rental denied - different location; moving fee")