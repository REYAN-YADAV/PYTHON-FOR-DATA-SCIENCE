# write a python program which accept any numberical value and print enen number
n = int(input("enter a number:  "))
if n>=0:
    for i in range(2,n+1,2):
        print(i)
else:
    print("Enter +ve number")

print("-"*50)
print("_"*50)

if n>=0:
    for i in range(1,n+1):
        if i%2==0:
            print(i)
else:
    print("Enter +ve number")
