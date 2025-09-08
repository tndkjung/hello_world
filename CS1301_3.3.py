#basic_for_loop.py

#In the designated areas below, write the three for loops
#that are described. Do not change the print statements that
#are currently there.

print("First loop:")
for i in range(1, 11):
    print(i)

#Write a loop here that prints the numbers from 1 to 10,
#inclusive (meaning that it prints both 1 and 10, and all
#the numbers in between). Print each number on a separate
#line.

print("Second loop:")
for i in range(-5, 6):
    print(i)

#Write a loop here that prints the numbers from -5 to 5,
#inclusive. Print each number on a separate line.

print("Third loop:")
for i in range(2, 21, 2):
    print(i)

#for i in range(1, 21):
#    if i % 2 == 0:
#        print("Third loop:", i)

#Write a loop here that prints the even numbers only from 1
#to 20, inclusive. Print each number on a separate line.
#
#Hint: There are two ways to do this. You can use the syntax
#for the range() function shown in the multiple-choice
#problem above, or you can use a conditional with a modulus
#operator to determine whether or not to print.





#for_loop.py
mystery_int = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#In math, factorial is a mathematical operation where an
#integer is multipled by every number between itself and 1.
#For example, 5 factorial is 5 * 4 * 3 * 2 * 1, or 120.
#Factorial is represented by an exclamation point: 5!
#
#Use a for loop to calculate the factorial of the number
#given by mystery_int above. Then, print the result.
#
#Hint: Running a loop from 1 to mystery_int will give you
#all the integers you need to multiply together. You'll need
#to track the total product using a variable declared before
#starting the loop, though!

#Add your code here!
factorial = 1 
for i in range(1, (mystery_int + 1)):
    factorial *= i
print(factorial)





#simple_for_each_loop.py
mystery_string = "CS1301"

#Write a for-each loop that lists each character in
#mystery_string with its index. For example, if the string
#was "David", the output would be:
#0 D
#1 a
#2 v
#3 i
#4 d
#
#Note that the first item is #0, the second is #1, and so
#on! We'll talk about why that is in Unit 4.
#
#Hint: You'll need a separate variable to keep track of how
#many letters you've printed! You may not use the range
#function on this problem.


#Add your code here!
number_of_letters = -1
for i in mystery_string:
    number_of_letters += 1
    print(number_of_letters, i)





#basic_while_loop.py
mystery_value = 87

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a while loop that continues to add 9 to mystery_value
#until mystery_value is greater than 100. Each time 9 is
#added, print the *new* value of mystery_value. For example,
#with mystery_value = 87, your code should print 96 and 105.

#Add your code here!
while mystery_value <= 100:
    mystery_value += 9
    print(mystery_value)





#three_while_loop.py
mystery_int_1 = 3
mystery_int_2 = 4
mystery_int_3 = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Above are three values. Run a while loop until all three
#values are less than or equal to 0. Every time you change
#the value of the three variables, print out their new values
#all on the same line, separated by single spaces. For
#example, if their values were 3, 4, and 5 respectively, your
#code would print:
#
#2 3 4
#1 2 3
#0 1 2
#-1 0 1
#-2 -1 0

#Add your code here!
while mystery_int_1 > 0 or mystery_int_2 > 0 or mystery_int_3 > 0:
    mystery_int_1 -= 1
    mystery_int_2 -= 1
    mystery_int_3 -= 1
    print(mystery_int_1, mystery_int_2, mystery_int_3)





#debug_factorial.py
num = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write some code below that will print the factorial of num.
#Remember to remove any debug statements when you're ready
#to submit for credit.

result = 1
for i in range(num):
    #print(i, result)
    result *= (i + 1)
print(result)





#beats_and_measures.py
beats_per_measure = 4
measures = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#In music, a song's time signature is given in terms of beats
#per measure. A common time signature is 4 beats per measure:
#for every measure of music, a conductor might count from 1
#to 4 with the tempo of the music.
#
#A song then has a number of measures. For example, a short
#song might have only 5 measures. In which case, a conductor
#would count from 1 to 4 five times. If the time signature had
#instead been 3 beats per measure, she would could from 1 to 3
#five times instead.
#
#Write a nested for loop that will print out the beats of the
#piece of music. For example, if the song had 4 beats per
#measure and only 2 measures, this would print out:
#
#1
#2
#3
#4
#1
#2
#3
#4
#
#We print from 1 to 4 before starting over because there are
#4 beats per measure, and we print them all twice because there
#are two measures.

#Add your code here! Using the original values of the variables
#above, this will initially print 1 through 4 five times for a
#total of 20 lines.
for i in range(measures):
    for beat in range(beats_per_measure):
        print(beat + 1)





#earworm.py
lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 6

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you have a song stuck in your head. Worse, you have
#only a few lines from a song stuck in your head. They just
#keep repeating over and over. The specific lines you have
#stuck in your head are stored in the variable lyrics.
#
#You can only stay sane so long while doing this.
#Specifically, you can only listen to lines_of_sanity lines
#before going crazy. Once you've reached lines_of_sanity,
#your brain will finish out the current list, then crumble.
#
#Write some code that will print the lyrics that run through
#your head. It should keep repeating each line one-by-one
#until you've reached lines_of_sanity lines. Then, it should
#keep going to finish out the current verse. After that, print
#"MAKE IT STOP" in all caps (without the quotes).
#
#HINT: Remember, we can iterate through items in a list using
#this syntax:
#
#  for item in list_of_items:
#
#HINT 2: You'll probably need a counter to count how many lines
#have been printed so far.

#Add your code here! Using the initial inputs from above, this
#should print 9 lines: all 4 lines of the list twice, followed
#by MAKE IT STOP

counter = 0
while counter < lines_of_sanity:
    for line in lyrics:
        print(line)
        counter += 1
print("MAKE IT STOP")