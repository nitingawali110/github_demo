
class Car():
    wheels=4
    def __init__(self,brand):
        self.brand=brand

    @staticmethod
    def sample():
        print(Car.wheels)

Car.sample()
