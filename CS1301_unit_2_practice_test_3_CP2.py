#weekend_plans.py
#This program suggests possible plans based on the weather and what kind of day it is.
is_weekend = True
is_holiday = False
is_rainy = False

print("Beach:", is_holiday and is_weekend and not is_rainy)
print("Lake:", is_weekend and not is_rainy)
print("Park:", not is_rainy)
print("Home:", is_rainy or (not is_weekend and not is_holiday))