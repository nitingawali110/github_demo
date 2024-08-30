try:
    print("Input First number: ")
    x=int(input())
    print("Input Second number: ")
    y=int(input())
    print(x/y)
except Exception as e:
    print(e)
else:
    print("In else block")
finally:
    print("This is always exeucted")
