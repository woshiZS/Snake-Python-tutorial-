people=['Kevin Durant','Kobe Bryant','Cai Cai']
for i in range(3):
    print(f"Dear {people[i]},could you please come and have dinner with me this evening?")

print(f'\nI am so sorry to inform that {people[1]} cant come.\n')
del(people[1])
people.insert(1,'Lebron James')
for i in range(3):
    print(f"{people[i]} is still in my list.")

print('\nI found a bigger table,so I will invite 3 more people.\n')

people.insert(0,'zmx')
people.insert(0,'Bear Ball')
people.append('One Piece')

for i in range(len(people)):
    print(f"Dear {people[i]},could you please come and have dinner with me this evening?")

print('\nSorry,my new dinner table wont arrive in time.')

size = len(people)-2
for i in range(size):
    temp=people.pop()
    print(f'{temp},I am sorry to inform you that I cant invite you to the dinner.')

for i in range(2):
    print(f'{people[i]},I am glad to tell you are still in the list')

del(people[0])
del(people[0])
print('\nThe party is over and the list is empty.')