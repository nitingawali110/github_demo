# override .if child class properties are matched with properties of parent class
# then properties in child class say to override to parent class

class A:
    a = 5

    def sample(self):
        print("sample method of class A")


class B(A):
    a = 50

    def sample(self):
        print("sample method of class B")

obj=B()
print(obj.a)
obj.sample()

