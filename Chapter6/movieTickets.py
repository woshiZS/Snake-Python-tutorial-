flag = True

while flag == True:
    age = int(input("Please input your age and I will tell your ticket payment.\nEnter a minus number or zero to quit.\n"))
    if age <=0:
        break 
    if age < 3:
        print("Your ticket is free of Charge.")
    elif age <= 12:
        print("Your ticket costs 10$.")
    elif age > 12:
        print("Your ticket cost 15$.")