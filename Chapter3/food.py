my_food=['pizzas','falafel','carrot cake']
friend_foods=my_food[:]
my_food.append('cannoli')
friend_foods.append('ice cream')
print("My favorite food are :")
for fd in my_food:
    print(fd)

print("My friend's favorite foods are :")
for  fd in friend_foods:
    print(fd)