# write a python program which sum of all number till n?

n = int(input("Enter a number: "))
if n<=0:
    print("enter a number greater than zero")
else:

    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
        print(i)
    else:
        print("sum of 1 to {} is {}".format(n, sum))

