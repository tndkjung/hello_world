#close_talker.py
#This program calculates the final price of an order based on the items included.
item = "quesadilla"
meat = "tofu"
queso = True
guacamole = False
double_meat = False

if item == "quesadilla":
    base_price = 4.0
elif item == "nachos":
    base_price = 4.5
elif item == "burrito":
    base_price = 5.0
    
if meat == "steak" or meat == "pork":
    base_price += 0.50
    #print("steak or pork")
if meat == "steak" and double_meat:
    base_price += 1.50
    #print("steak and double meat")
elif meat == "pork" and double_meat:
    base_price += 1.50
    #print("pork and double meat")
elif double_meat:
    base_price += 1.0
    #print("double meat")

if guacamole:
    base_price += 1.0
    #print("guac")

if queso and not item == "nachos":
    base_price += 1.0
    #print("queso")
    
print(base_price)


#outfit.py
#This program suggests an outfit based on the weather using nested conditionals.
sunny = True
windy = False

if sunny:
    if not windy:
        print("Wear a hat!")
    else:
        print("Enjoy the breeze!")


#password_check.py
#This program determines if a login is successful based on the entered password and number of tries.
entered = "abc123"
password = "abc123"
tries = 3

if tries <= 3:
    if entered == password:
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Tries exceeded.")


#tea_time.py
#This program suggests a type of tea to buy based on our mood.
mood = "impatient"

cost = "free"
if mood == "sad":
    tea = "oolong"
    cost = 3.99
elif mood == "anxious":
    tea = "green tea"
    cost = 5.45
elif mood == "tired":
    tea = "english breakfast"
    cost = 4.35
else:
    tea = None

print(tea)
print(cost)