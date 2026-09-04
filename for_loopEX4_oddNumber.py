#write a python program which accept any numberical value generate odd number

n = int(input("Enter a number: "))
if n>=0:
    for i in range(1,n+1,2):
        print(i)
else:
    print("enter +ve number")
