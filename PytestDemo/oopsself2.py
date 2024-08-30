
class Car:
    wheels=4

    def start_car(self):
        print("car started")

    def example(self):
        print(self.wheels)
        self.start_car()

car1=Car()

print(car1.wheels)
car1.start_car()
car1.example()
