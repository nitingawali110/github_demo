class A:
    __a =5

    def __sample(self):
        print("Inside the method of class A")

    def printdetails(self):
        print(self.__a)
        self.__sample()

obj= A()
obj.printdetails()

