def make_car(manufacture,model,**car_info):
    car_info['brand']=manufacture
    car_info['model']=model
    return car_info

car_0 = make_car('sabaru','outback',color = 'blue',two_packeges = True)
print(car_0)