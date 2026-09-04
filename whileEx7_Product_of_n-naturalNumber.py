# Write a python program which will calculate product of n-natural number?

n = int(input("enter the number: "))
if n>0:
    pro = 1
    i = 1
    while(i<=n):
        pro = pro*i
        i+=1
    else:
        print("product of {} natural numbers is {}".format(n,pro))
else:
    print("Enter a positive integer")
