rivers={'Nile':'Egypt','Yangtze':'China','Amazon River':'Brazil'}
for river,country in rivers.items():
    print(f"The {river} runs through {country}.")
print(" ")
for river in rivers:
    print(river)
print(" ")
for country in rivers.values():
    print(country)