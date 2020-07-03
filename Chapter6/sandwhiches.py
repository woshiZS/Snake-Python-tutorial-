orders = ['Bacon Sandwhich','Beef Sandwhich','Cheese Sandwhich','pastrami','pastrami','pastrami']

print("Sorry,pastrami has been sold out.")
finished = []
while 'pastrami' in orders:
    orders.remove('pastrami') 

while orders:
    sandwhich = orders.pop()
    print(f"I made your {sandwhich}.")
    finished.append(sandwhich)

print("I have made all the sandwhiches.")
for sandwhich in finished:
    print(sandwhich)