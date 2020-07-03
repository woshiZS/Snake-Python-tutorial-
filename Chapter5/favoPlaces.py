place_0=['Chang Sha','Heng Yang','Tian Jin']
place_1=['Bei Jing','Guan Zhou']
place_2=['Shang Hai','Sheng Zheng']

favo_places={'Jason':place_0,'Bob':place_1,'Reckless':place_2}

for person,places in favo_places.items():
    print(f"{person} :")
    for place in places:
        print(f"\t{place}")