class A:  # Parent Class
    a = 10

    def methos_a(self):
        print("Indisde Method A")


class B(A):  # Child Class
    b = 5

    def method_b(self):
        print("Inside Methos B")


obj = B()
print(obj.a)
print(obj.b)
