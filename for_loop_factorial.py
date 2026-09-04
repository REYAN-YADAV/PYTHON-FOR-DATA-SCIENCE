# write a python program which find factorial of n?

n = int(input("Enter a number: "))
if n<0:
    print("enter a number greater than zero")
else:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    else:
        print("factorial of {} is {}".format(n, fact))

