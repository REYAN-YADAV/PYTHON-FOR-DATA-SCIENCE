# write a python program which product of all number till n?

n = int(input("Enter a number: "))
if n<=0:
    print("enter a number greater than zero")
else:

    pro = 1
    for i in range(1, n + 1):
        pro = pro*i
        print(i)
    else:
        print("product of 1 to {} is {}".format(n, pro))

