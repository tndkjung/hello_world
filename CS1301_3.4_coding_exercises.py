#print_math_symbols.py
#When writing out mathematical equations for younger
#audiences, we usually want to use the traditional division
#and multiplication symbols, ÷ and ×, instead of slashes and
#asterisks. These keys aren't on the keyboard, though. So,
#let's write functions that will print them.
#
#First, write two functions: one called print_division_symbol
#and one called print_multiplication_symbol. The functions
#should do what their names suggest: print_division_symbol
#should print a division symbol, print_multiplication_symbol
#should print a multiplication symbol. You can copy the
#characters for those symbols from these directions.
#
#Then, after writing those two functions, call them in the
#same order: print_division_symbol, then
#print_multiplication_symbol. The output of your code should
#thus be ÷, then ×, each on their own line.
#
#Note that you don't need to worry about the end="" thing
#you saw in the video: just print the symbols on their own
#lines. Note also that if you receive a UnicodeEncodeError,
#try submitting your code instead of running it: that error
#happens sometimes, but only affects Run, not Submit.
#
#HINT: you're writing two functions. You don't want one to
#be inside the other.

#Write your two functions here!
def print_division_symbol():
    print("÷")
    
def print_multiplication_symbol():
    print("×")

#Call your two functions here!
print_division_symbol()
print_multiplication_symbol()





#print_stuff.py
#Take a look at the three functions completely written
#below. It's your job to correctly call each function with
#the following parameters:
#
#  Function 1: the string "Black Horse and a Cherry Tree" 
#  Function 2: no parameters
#  Function 3: these five numbers: 80, 80, 95, 86, 79

#Function 1
def cherry_pie(song):
    if ("Cherry" in song):
        print("Sheee's my cherry pie")
    else:
        print("Huh... must be an American Pie.")

#Function 2
def should_I_go_to_Waffle_House():
    print(True)

#Function 3
def average_grades(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    average = sum / 5
    print(average)

#Add your function calls here! Don't change any of the
#code above.
cherry_pie("Black Horse and a Cherry Tree")
should_I_go_to_Waffle_House()
average_grades(80, 80, 95, 86, 79)





#retunr_date.py
#Write a function called get_todays_date that returns
#today's date as a string, in the form year/month/day.
#For example, if today is January 15th, 2017, then it
#would return 2017/1/15.
#
#Remember, you took care of the string formatting part of
#this exercise in 2.2.9 Coding Exercise 1! Now, you're
#converting it to a function that returns the string.
#
#Note that the line below will let you access today's date
#using date.today() anywhere in your code.
from datetime import date

#Write your function here!
def get_todays_date():
    myDate = date.today()
    return(str(myDate.year) + "/" + str(myDate.month) + "/" + str(myDate.day))

#If you want to test your code, you can do so by calling
#your function below. However, this is no longer required
#for grading.
print(get_todays_date())





#square_area.py
#Write a function that takes in one integer parameter, the
#side length of a square, and returns the area. The function
#should be named find_area, and have one parameter:
#side_length.

#Write your function here!
def find_area(side_length):
    result = side_length ** 2
    return result

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "A square with side length 4 has an area of 16".
test_side_length = 4
print("A square with side length", test_side_length, "has an area of", find_area(test_side_length))





#my_TAs.py
#Helping us develop this class are a team of teaching
#assistants, often called TAs for short.
#
#Write a function called my_TAs. The function should take as
#input three strings: first_TA, second_TA, and third_TA. It
#should return as output the string, "[first_TA], [second_TA],
#and [third_TA] are awesome!", with the values replacing the
#variable names.
#
#For example, my_TAs("Sridevi", "Lucy", "Xu") would return
#the string "Sridevi, Lucy, and Xu are awesome!"
#
#Hint: Notice that because you're returning a string instead
#of printing a string, you can't use the print() statement
# -- you'll have to create the string yourself, then return
#it!


#Write your function here!
def my_TAs(first_TA, second_TA, third_TA):
    return str(first_TA) + ", " + str(second_TA) + ", and " + str(third_TA) +" are awesome!"    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "Joshua, Jackie, and Marguerite are awesome!".
test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))





#hello_there.py
#Write a function called greeting. greeting should have one
#parameter, a string representing a name. It should return
#a string with the message "Hi [name]!", where the value of
#the parameter is used in place of [name].
#
#For example:
#
# greeting("David") -> "Hi David!"

def greeting(input_name):
    return "Hi " + input_name + "!"

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "Hi David!"

a_name = "David"
message = greeting(a_name)
print(message)





#total_volue.py
#Write a function called total_volume. total_volume should
#have four parameters, all integers. The first three
#parameters should represent the length, width, and height
#of a box respectively. The fourth should represent the
#number of boxes.
#
#The function should return an integer representing the
#total volume represented by the given boxes. For example,
#if the length is 10, the width is 2, the height is 2, and
#there are 4 boxes, then the total volume would be 160:
#((10 * 2 * 2) * 4) = 160.
def total_volume(length, width, height, box_count):
    return length * width * height * box_count

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 160
test_length = 10
test_width = 2
test_height = 2
test_box_count = 4
result = total_volume(test_length, test_width, test_height, test_box_count)
print(result)





#swapped.py
#Below we've written a function that is supposed to take in
#four parameters and produce a string representing the cost
#of a person's weekly soda consumption. Below the function
#definition, we're calling the function.
#
#However, right now, the code is erroring out. Fix this code
#without changing the code inside the function. You may
#change either the function declaration (on line 11) or the
#function call on line 27.

def soda_habit(sodas_per_week, price_per_soda, calories_per_soda, preferred_soda):
    
    #Above, we've moved preferred_soda to the beginning and
    #sodas_per_week to the end, so our original function
    #call will work.
    
    #Don't change the body of this function!
    
    money_spent = price_per_soda * sodas_per_week
    calories_consumed = calories_per_soda * sodas_per_week
    
    summary_string = "You're spending $" + str(money_spent) + " on " + preferred_soda + " per week! "
    summary_string += " That's " + str(calories_consumed) + " calories!"
    
    return summary_string

result = soda_habit(9, 1.75, 140, "Coca-Cola")
print(result)





#reverse_string.py
#We've written the function, reverse, below. This function
#takes a string and returns the reverse of it. There are two
#scope errors somewhere in the code. Read through all the
#code below to find and fix the errors, so that the function
#produces the correct output and the result of the function
#is correctly printed. Note that you should not change the
#three lines that are already present in the function, but
#you may add lines before them, or you may change or add to
#the lines outside the function.
#
#Note that your goal here is to fix both the function itself
#and the program as a whole. So, your function should be
#able to be called on a new string, and the program when
#run should print the reverse of the string originally on
#line 29.

def reverse(a_string):
    #You may add code before the following three lines.
    rev = ""
    
    #Don't change these three lines.
    for i in range(len(a_string)-1, -1, -1):
        rev = rev + a_string[i]
    return rev

#You may change or add to the following lines.
reversed_string = reverse("This string should be reversed!")
print(reversed_string)





#snowed_in.py
#Write a function called snowed_in that will determine
#whether school is closed based on the weather and
#temperature. We'll pretend the school is in Georgia, where
#a little snow or sub-freezing temperatures are enough to
#close down schools!
#
#The function should take three parameters:
#
# - temperature, a float
# - weather, a string
# - is_celsius, a boolean
#
#The function should return True if temperature is below
#freezing (32 if is_celsius is False, 0 if is_celsius is
#True) or if weather is "snowy". Otherwise, it should
#return False.
#
#Note, however, that is_celsius should be an optional
#argument. If the function call does not supply a value for
#is_celsius, assume it is True.
#
#For example:
#
# snowed_in(15, "sunny") -> False
# is_celsius is assumed to be True, so 15 is not below
# freezing.
#
# snowed_in(15, "sunny", is_celsius = False) -> True
# is_celsius is False, so 15 is below freezing.
#
# snowed_in(15, "snowy", is_celsius = True) -> True
# The weather is "snowy", so the temperature doesn't matter.

#Write your function here!
def snowed_in(temp, weather, is_celsius = True):
    if weather == "snowy":
        return True
    else:
        if is_celsius == True:
            if temp  < 0:
                return True
            else:
                return False
        else:
            if temp < 32:
                return True
            else:
                return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print False, True, and True, each on their own line.

print(snowed_in(15, "sunny")) #Should print False
print(snowed_in(15, "sunny", is_celsius = False)) #Should print True
print(snowed_in(15, "snowy", is_celsius = True)) #Should print True