# Write a python program which will find sum of n natural number?

n = int(input("Enter a number: "))
if n>0:
    sum = 0
    i = 1
    while (i <= n):
        sum = sum + i
        print(i)
        i = i + 1
    else:
        print("sum of natural numbers is: {}".format(sum))

else:
    print("enter +ve number")