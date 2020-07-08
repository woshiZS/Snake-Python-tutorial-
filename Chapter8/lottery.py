from random import choice

candidate=(0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e')
my_tickets=['bcaa','1234','0789']
times=0

while True:
    target=''
    for i in range(4):
        target+=str(choice(candidate))
    
    times+=1

    if target in my_tickets:
        print(f"After {times} time I finally won the prize! and the lottery code is {target}.")
        break
