# oops, basic concept
# The below is the fucntion in python beacuse it is created outside the class
def sample_fun():  #
    print("Inside sample function")

sample_fun()

class Car:
    wheels=4

    # below is the method in python
    def start_car(self):
        print("Car Started")

    def stop_car(self):
        print("Car stoped")

# The below is the object creation statement

hamaze=Car()
svid=Car()
hamaze.start_car()
print(hamaze.wheels)
print(svid.wheels)

svid.stop_car()
