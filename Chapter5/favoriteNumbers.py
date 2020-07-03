favo_number={'James':[23,6],'Durant':[35,7],'Irving':[2,11],'Kobe':[8,24]}
for name,numbers in favo_number.items():
    print(f"Below are {name}'s favorite numbers : ")
    for number in numbers:
        print(f"\t{number}")
