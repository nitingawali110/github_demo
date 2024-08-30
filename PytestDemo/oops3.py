# Assigning method parameters to class variable using self keyword

class Car:

    def sample(self, brand, model, price, milage):
        print(brand, model, price, milage)
        self.brand = brand
        self.model= model
        self.price = price
        self.milage = milage

    def sample_two(self):
        print(self.brand,self.model,self.price,self.milage)

car1 = Car()

car1.sample("Tata", "Tata Punch", 100000, 50)
car1.sample_two()
