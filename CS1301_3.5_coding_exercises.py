#try_except.py
mystery_value = "9"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Create a program that divides 10 by mystery_value and prints
#the result. In the case that an error occurs, print "Not
#possible".
#
#Use error handling to determine if an error will occur; do
#not use the type() function. You might be surprised how many
#types Python can divide by 10!

#Add your code here!
try:
    result = 10 / mystery_value
    print(result)
except:
    print("Not possible")





#try_except_2.py
mystery_value = 9

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Create a program that divides 10 by mystery_value and prints
#the result. In the case that mystery_value is equal to 0,
#print "Not possible". Do not catch any other errors. This
#means there will be an uncaught error in the correct answer!
#
#You may not use any conditionals or the type() function.

#Add your code here!
try:
    result = 10 / mystery_value
    print(result)
except ZeroDivisionError:
    print("Not possible")





#try_except_3.py
mystery_value = 9

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Create a program that divides 10 by mystery_value and 
#prints the result. In the case that mystery_value is 
#equal to 0, print "Can't divide by zero". If for any other
#reason the operation fails, print "Not possible".
#
#You may not use any conditionals or the type() function.

#Add your code here!
try:
    result = 10 / mystery_value
    print(result)
except ZeroDivisionError as error:
    print("Can't divide by zero")
except Exception as error:
    print("Not possible")





#buy_a_vowel.py
#Write a function called has_a_vowel. has_a_vowel should have
#one parameter, a string. It should return True if the string
#has any vowels in it, False if it does not.

def has_a_vowel(a_str):
    #print("Starting...")
    string = ""
    for letter in a_str:
        #print("Checking", letter)
        if letter in "aeiou":
            #print(letter, "is a vowel, returning True")
            string += letter
        else:
            #print(letter, "is not a vowel, returning False")
            string += ""
    if len(string) > 0:
        return True
    else:
        return False
    print("Done!")
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then True, then False, then False, each on
#its own line.
print(has_a_vowel("abba"))
print(has_a_vowel("beeswax"))
print(has_a_vowel("syzygy"))
print(has_a_vowel(""))





#try_except_4.py
#Right now, the code below will encounter an error when num
#is 0, but it will not print anything when it does, and then
#it will keep running for num = 1, num = 2, and num = 3
#afterwards. Modify this code so that once it hits an error,
#the loop stops altogether.
#
#You still should not print anything when the error is
#encountered, and the loop definition on line 10 should not
#be changed.

try:
    for num in range(-3, 3):
	    print(5 / num)
except:
    pass





#get_interger.py
#Write a function called get_integer that takes as input one
#variable, my_var. If my_var can be converted to an integer,
#do so and return that integer. If my_var cannot be converted
#to an integer, return a message that says, "Cannot convert!"
#
#For example, for "5" as the value of my_var, get_integer would
#return the integer 5. If the value of my_var is the string
#"Boggle.", then get_integer would return a string with the
#value "Cannot convert!"
#
#Do not use any conditionals or the type() function.

#Write your function here!
def get_integer(my_var):
    try:
        result = int(my_var)
        return result
    except:
        return "Cannot convert!"

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5, Cannot convert!, and 5.

print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))





#get_integer_2.py
#This exercise is identical to the previous exercise,
#except that instead of printing "Cannot convert!" when my_var
#cannot be converted to an integer, you should instead return
#the error message that results. For a reminder of how to
#access the error message in the except block, check out
#3.5.3, specifically CatchingASpecificError-4.py from 3.5.3.3
#and CatchingMultipleSpecificErrors-5.py from 3.5.3.4.
#
#Write a function called get_integer that takes as input one
#variable, my_var. If my_var can be converted to an integer,
#do so and return that integer. If my_var cannot be converted
#to an integer, return the error message that results from
#attempting to do so.
#
#Do not use any conditionals or the type() function.

#Write your function here!
def get_integer(my_var):
    try:
        result = int(my_var)
        return result
    except Exception as error:
        return error

#You can use the lines below to test out your function. When
#the function is written correctly, the output of these three
#lines should be:
#5
#invalid literal for int() with base 10: 'Boggle.'
#5
print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))