# making_change.py
#This program calculates the change to be returned to a customer after a purchase.
total = "5.45"
cash = "10.0"

change = float(cash) - float(total)
change = round(change, 2)
print("Your change is:", change)


#boolean_beverage_recs.py
#This program recommends beverages based on weather and time of day.
hot = True
cold = False
morning = True
evening = False
night = False

print("Coffee:", morning or (cold and evening))
print("Hot Tea:", cold and (evening or night))
print("Smoothie:", hot)
print("Milkshake:", (hot and evening) or night)


#time_of_birth.py
#This program generates a birth announcement based on given information.
parent_1 = "Caitlin"
parent_2 = "David"
baby = "Lucy"
month = "January"
day = 2
year = 2015
time = "11:12PM"

print(baby + " was born to " + parent_1 + " and " + parent_2 + " at " + month + " " + str(day) + ", " + str(year) + " at " + time + ".")


#savings_goals.py
#This program checks if an investment will meet a savings goal.
principal = 40000
rate = 0.05
years = 5
goal = 50000
from math import e

value = principal * e ** (rate * years)
print(value >= goal)


#convert_from_binary.py
#This program converts a binary number to its decimal equivalent.
number = 1101

dec_number = (number >= 10000000) * 128
number -= (number >= 10000000) * 10000000
dec_number += (number >= 1000000) * 64
number -= (number >= 1000000) * 1000000
dec_number += (number >= 100000) * 32
number -= (number >= 100000) * 100000
dec_number += (number >= 10000) * 16
number -= (number >= 10000) * 10000
dec_number += (number >= 1000) * 8
number -= (number >= 1000) * 1000
dec_number += (number >= 100) * 4
number -= (number >= 100) * 100
dec_number += (number >= 10) * 2
number -= (number >= 10) * 10
dec_number += (number >= 1) * 1
print(dec_number)


#much_wow.py
#This program prints a repeated message with punctuation using given volues.
message = "lol"
punct = "!"
num = 3

print(((message * num) + punct) * (num - 1) + (message * num))


#root_squared.py
#This program calculates the square and square root of a number,
#then prints the square a number of times equal to the square root.
num = 4

sqr = num ** 2
sqrt = int(num ** 0.5)
print(str(sqr) * sqrt)


#happy_birthday.py
#This program calculates the current age of a person based on their birth date and the current date.
current_day = 31
current_month = 5
current_year = 2018
birth_day = 19
birth_month = 12
birth_year = 1990

birthday_not_passed = current_month < birth_month or (current_month == birth_month and current_day < birth_day)
current_age = current_year - birth_year - birthday_not_passed
print(current_age)





