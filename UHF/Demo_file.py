# Outside the class-It is Called Function
def sample_fun():
    print("Inside Sample Function")
sample_fun()


class Car:
    wheels = 4
   # If the same function is created inside the class it called Method
    def start_car(self):
        print("Car Started")

# The Below is the object Creations Statement
Car()

# Object Reference
Amaze=Car()
print(Amaze.start_car())

print(Amaze.wheels)
sample_fun()
