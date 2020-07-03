response = {}

polling_active = True

while polling_active:
    name = input("What is your name?\n")
    moutain = input("Which moutain would you like to climb?\n")

    response[name] = moutain
    repeat = input("Continue?(yes/no)")

    if repeat == 'no':
        polling_active = False

print("\n--------------- Poll Results ------------------- ")
for name,moutain in response.items():
    print(f"{name} would like to climb {moutain}.")