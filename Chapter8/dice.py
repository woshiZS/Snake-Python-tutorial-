from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        print(randint(1,self.sides))

die_0=Die()
die_1=Die(10)
die_2=Die(20)

print(f"\nBelow is a {die_0.sides} dice.")
for i in range(10):
    die_0.roll_die()

print(f"\nBelow is a {die_1.sides} dice.")
for i in range(10):
    die_1.roll_die()

print(f"\nBelow is a {die_2.sides} dice.")
for i in range(10):
    die_2.roll_die()