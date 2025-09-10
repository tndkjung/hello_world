#front_times.py
#Given a string and a non-negative int n, we'll say that the
#"front" of the string is the first 3 chars, or whatever is
#there if the string is less than length 3. Return n copies
#of the front.

str = "Chocolate"
n = 2

front = ""
digits = 0

#Method 1
for i in str:
    front += i
    digits = len(front)
    if digits == 3:
        break
print(front * n)

#Method 2
for i in str:
    digits = len(front)
    if digits < 4:
        front += i

print(front * n)

#Method 3
for i in range(3):
    front += str[i]

print(front * n)





#string_bits.py
#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

str = "Hello"

string = ""

for i in range(0, len(str), 2):
    string += str[i]

print(string)