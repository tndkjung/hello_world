#round_up_the_change.py
#This program calculates the total cost after rounding up and donation.
original_total = "5.45"
donation = "0.55"

final_total = float(original_total) + float(donation)
final_total = int(final_total)
print("Your total is $" + str(final_total) + " and you donated $" + str(donation))
print(f"Your total is ${final_total} and you donated ${donation}")