#factors.py
#This program checks if one integer is a factor of another.
mystery_int_1 = 15
mystery_int_2 = 5

if mystery_int_1 % mystery_int_2 == 0 or mystery_int_2 % mystery_int_1 == 0:
    print("Factors!")


#factors_2.py
#This program checks if one integer is a factor of another.
mystery_int_1 = 15
mystery_int_2 = 5

if mystery_int_1 % mystery_int_2 == 0 or mystery_int_2 % mystery_int_1 == 0:
    print("Factors!")
else:
    print("Not factors :(")


#snow_days.py
#This program checks the state and prints a message about school.
mystery_state = "North Carolina"

if mystery_state == "New Jersey":
    print("School isn't cancelled.")
elif mystery_state == "North Carolina":
    print("School is postponed.")
elif mystery_state == "Georgia":
    print("School is cancelled!")
else:
    print("idk wear a sweater")
    

#freezing.py
#This program checks if a temperature is freezing.
temperature = -3.7
celsius = True

if celsius == True and temperature <= 0:
    print("Freezing")
elif celsius != True and temperature <= 32:
    print("Freezing")
else:
    print("Not freezing")
    

#zzz.py
#This program checks a string for consecutive z's.
mystery_string = "zizazzle"

if "zzz" in mystery_string:
    print("I'm sleepy...")
elif "zz" in mystery_string:
    print( "I love ZZ Top!")
elif "z" in mystery_string:
    print("One is the loneliest number.")
else:
    print("Who needs z anyway?")


#who_won.py
#This program checks the scores of two teams and prints who won.
team_1 = "Georgia Tech"
team_1_score = 28
team_2 = "Georgia"
team_2_score = 27

if team_1_score > team_2_score:
    print(team_1, "beat", team_2, "by", str(team_1_score - team_2_score))
elif team_2_score > team_1_score:
    print(team_2, "beat", team_1, "by", str(team_2_score - team_1_score))
else:
    print(team_1, "played", team_2, "and it was a tie")