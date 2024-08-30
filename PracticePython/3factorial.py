factorial = 1
num = 5

if num < 0:
    print("Factorial does not exists for negative number")
elif num == 0:
    print("the factorial 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

print("Factorial of", num, "is", factorial)

print("---"*20)


def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

num=5
print(fact(num))

print("---"*20)

def fact1(m):
    return 1 if (m==0 or m==1) else m*fact1(m-1)

num1=5
print(fact1(num1))
