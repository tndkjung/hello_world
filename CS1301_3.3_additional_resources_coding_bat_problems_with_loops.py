#front_times.py
#Given a string and a non-negative int n, we'll say that the
#"front" of the string is the first 3 chars, or whatever is
#there if the string is less than length 3. Return n copies
#of the front.

str = "Chocolate"
n = 2

front = ""
digits = 0

for i in str:
    front += i
    digits = len(front)
    if digits == 3:
        break
print(front * n)