# Single Inheritance
class A:
    a = "Class A"


class B(A):
    b = "Class B"


obj = B()
print(obj.a)
print(obj.b)
print("-" * 50)


# Multilevel Inheritance
class P:
    a = 9


class Q(P):
    b = 10


class R(Q):
    c = 10


obj = R()
print(obj.a)
print(obj.c)
print("-" * 50)


# Hierarchical Inheritance
class A:
    a = 1.1
    print("Hierarchical class A ")


class B(A):
    b = 1.2
    print("Hierarchical class B ")


class C(A):
    c = 1.3
    print("Hierarchical class B ")


obj = C()
obj1 = B()
print(obj.a)
print(obj1.a)
print("-" * 50)


# Multiple
class A:
    a = "Class A"


class B():
    b = "Class B"


class c(A, B):
    c = "class C,A,B"


obj3 = c()
print(obj3.a)
print(obj3.b)
print("-" * 50)
