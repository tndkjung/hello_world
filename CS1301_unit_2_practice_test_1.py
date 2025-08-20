#adding_strings.py
#This program finds the numeric sum of two strings representing numbers.
mystery_string_1 = "17"
mystery_string_2 = "9"

mystery_sum = int(mystery_string_1) + int(mystery_string_2)
print("The sum of the two strings is", mystery_sum)


#boolean_meal_recs.py
#This program recommends meals based on weather and time of day.
hot = True
cold = False
morning = True
evening = False
night = False

print("Soup:", cold and (evening or night))
print("Biscuit:", morning and cold)
print("Cereal:", (morning and hot) or night)
print("Pizza:", evening or night)


#cuckoo_clock.py
#This program prints a cuckoo clock announcement based on the current time.
current_hour = 5
time_of_day = "PM"

print("The current time is " + str(current_hour) + str(time_of_day) + ": " + str("Cuckoo!" * int(current_hour)))


#total_mortgage.py
#This program calculates the total cost of a mortgage based on given information.
cost = 150000
rate = 0.0415
years = 15

monthly_rate = rate / 12
number_of_months = years * 12
total_amount = cost * (number_of_months) * (monthly_rate) / (1 - ((1 + monthly_rate) ** -number_of_months))
#print(total_amount)
total_amount = round(total_amount, 2)
print("The total cost of the house will be $" + str(total_amount))


#convert_to_binary.py
##This program converts a decimal number to its binary equivalent.
number = 215

first_dgt = int(number // 128)
number %= 128
second_dgt = int(number // 64)
number %= 64
third_dgt = int(number // 32)
number %= 32
fourth_dgt = int(number // 16)
number %= 16
fifth_dgt = int(number // 8)
number %= 8
sixth_dgt = int(number // 4)
number %= 4
seventh_dgt = int(number // 2)
number %= 2
eighth_dgt = int(number // 1)

print(str(first_dgt) + str(second_dgt) + str(third_dgt) + str(fourth_dgt) + str(fifth_dgt) + str(sixth_dgt) + str(seventh_dgt) + str(eighth_dgt))


#much_neato.py
##This program prints a message with repeated patterns based on given variables.
message = "lol"
punct = "!"
num = 3

print((((punct * num) + message) * num) + punct * num)


#square_rooted.py
#This program prints the root the square number of times.
num = 4

sqr = num ** 2
sqrt = int(num ** 0.5)
print(str(sqrt) * sqr)


#due_date.py
#This program checks if an assignment is still eligible for submission based on the current time and due time.
current_hour = 3
current_minute = 54
current_section = "AM"
due_hour = 5
due_minute = 15
due_section = "AM"

same_section = current_section == due_section
same_hour = current_hour == due_hour

condition_1 = same_section and same_hour and (current_minute < due_minute)
condition_2 = same_section and not same_hour and (current_hour == 12 or (current_hour < due_hour and due_hour != 12))
condition_3 = current_section < due_section
print(condition_1 or condition_2 or condition_3)