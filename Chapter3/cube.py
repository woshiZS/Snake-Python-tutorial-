cubes=[value for value in range(1,11)]
for cube in cubes:
    print(cube)

print("The first 3 items in the list are : ")
for num in cubes[:3]:
    print(num)

print("Three items from the middle of the list are : ")
for num in cubes[4:7]:
    print(num)

print("The last 3 items in the list are : ")
for num in cubes[-3:]:
    print(num)