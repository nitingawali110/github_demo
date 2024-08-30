class Car():
    wheels=4

    def start_car(self):
        print("Car Started")

    def stop_car(self):
        print("Car Stopped")
        print(self.wheels)

car1=Car()

print(car1.wheels)
print(car1.start_car())
print(car1.stop_car())
