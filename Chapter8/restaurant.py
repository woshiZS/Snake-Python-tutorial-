class Restaurant:
    '''Model a real restaurant'''

    def __init__(self,res_name,cuisine_type):
        '''Init an instance'''
        self.number_served=0
        self.res_name=res_name
        self.cuisine_type=cuisine_type
    
    def describe_res(self):
        print(f"The restaurant is called {self.res_name}.")
        print(f"And their cuisine type is {self.cuisine_type}.")

    def open_res(self):
        '''indicate the restaurant is open'''
        print(f"{self.res_name} is open today!")

    def set_number_served(self,num):
        self.number_served=num

    def increment_number_served(self,increment):
        self.number_served+=increment

if __name__=="__main__":
    my_res=Restaurant('Haidilao','Hotpot')
    print(my_res.res_name)
    print(my_res.cuisine_type)

    my_res.open_res()
    my_res.describe_res()

    res_1=Restaurant('Yang Daye','Shuan Rou')
    res_2=Restaurant('KFC','Fast food')

    res_1.describe_res()
    res_2.describe_res()

    print(my_res.number_served)
    my_res.number_served=10
    print(my_res.number_served)
    my_res.set_number_served(20)
    print(my_res.number_served)
    my_res.increment_number_served(5)
    print(my_res.number_served)

class IceCreamStand(Restaurant):

    def __init__(self, res_name, cuisine_type):
        super().__init__(res_name, cuisine_type)
        self.flavors=['Blue Berry','Matcha','SweetGrass']

    def describe_flavors(self):
        for flavor in self.flavors:
            print(flavor)

if __name__=="__main__":
    bobby_ice = IceCreamStand('Bobby Ice','icecream')
    bobby_ice.describe_flavors() 