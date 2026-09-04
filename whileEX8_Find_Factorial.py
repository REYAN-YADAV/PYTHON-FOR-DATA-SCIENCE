# Write  the python program which will calculate factorial of a given number?

n = int(input("Enter a number: "))
if n>=0:
    fact = 1
    i = 1
    while (i<=n):
        fact = fact*i
        i = i+1
    else:
        print("factorial of {} is {}".format(n,fact))
else:
    print("Enter a positive integer")
