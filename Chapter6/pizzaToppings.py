flag = True

while flag == True :
    order=input("Please enter your pizza topping.\nEnter quit to end ordering.\n")
    if order == 'quit':
        flag = False
    else :
        print(f"{order} has been already added to your pizza toppings.")