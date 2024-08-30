class A:
    a=5
    def sample(self):
        print("Inside sample method of class A")

class B(A):
    a=10
    def sample(self):
        print("inside sample method of class B")

obj1=B()
print(obj1.a)
obj1.sample()

print("--"*50)

# method Overloading

class A:

    def sample(self,a=None,b=None):
        if a!=None and b!=None:
            print(a*b)
        elif a!=None:
            print(a)
        else:
            print("Nothing")
obj3=A()
print(obj3.sample(a=50))
print("--"*50)
