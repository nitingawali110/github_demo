class car():
    wheels=4

    def sample(self,brand,model,price,milage):
        self.brand=brand
        self.model=model
        self.price=price
        self.milage=milage
        print(brand,model,price,milage)

    def sample_two(self):
        print(self.brand,self.model,self.price)

car1=car()
car1.sample("Honda","Amaze",90000,14.5)
car1.sample_two()

