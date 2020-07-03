city_0={'country':'China','population':"300W",'fact':'Mountain Heng locates here.'}
city_1={'country':'China','population':'600W','fact':'A good place for entertainment.'}
city_2={'country':'China','population':'700W','fact':'Nankai University locates here.'}

cities={'Heng Yang':city_0,'Chang Sha':city_1,'Tian Jin':city_2}

for city,infos in cities.items():
    print(city)
    for k,v in infos.items():
        print(f"\t{k} : {v}")


