pet_0={'Kind':'Cat','Owner':'Lucy'}
pet_1={'Kind':'Dog','Owner':'Jason'}
pet_2={'Kind':'Fish','Owner':'Bob'}

pets=[pet_0,pet_1,pet_2]

for pet in pets:
    print(" ")
    for key,value in pet.items():
        print(f"{key} : {value}")