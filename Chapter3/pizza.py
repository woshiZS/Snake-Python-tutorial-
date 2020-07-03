pizzas=['sweet','pepperoni','salty']
for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really love pizza!\n")

friend_pizzas=pizzas[:]
pizzas.append('canonia')
friend_pizzas.append('ice cream')

print("My favorite pizzas are :\n")
for pz in pizzas:
    print(pz)

print("My friend's favorite pizza are :\n")
for pz in friend_pizzas:
    print(pz)