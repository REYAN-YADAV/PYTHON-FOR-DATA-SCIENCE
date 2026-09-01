#Write a python program wchich accept two numerical value and find big and check for equality?
try:
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))
    big = a if a > b else b if b > a else "Both value are equal"
    print("big({},{}) = {}".format(a,b,big))
except ValueError:
    print("Please don't enter alnum,str and symbol")
