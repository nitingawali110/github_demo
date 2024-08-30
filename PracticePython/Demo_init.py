class car():
    wheels=4

    def __init__(self,brand,model,price,milage):
        self.brand=brand
        self.model=model
        self.price=price
        self.milage=milage
        print(brand,model,price,milage)

    def sample_two(self):
        print(self.brand,self.model,self.price)

car1=car("Honda","Amaze",90000,14.5)


