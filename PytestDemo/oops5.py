class A:
    a=9

class B(A):
    b=10

class C(A):
    c=11

class D(B,C):
    d=14

obj=D()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)
