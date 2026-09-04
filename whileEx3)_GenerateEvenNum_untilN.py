# Write a python program which will generate all even number until n where n is +ve

n = int(input("Enter a number: "))
i = 2
while (i <= n):
     print(i)
     i = i + 2
else:
     print("Thank you for using this program")


# Write python program which will generaate all even number from n to 2 whwre n is +ve

n = int(input("Enter a number: "))
if (n % 2 == 0):
    i = n
    while (i>=2):
        print(i)
        i = i - 2
    else:
        print("Thank you for using this program")
else:
    i = n-1
    while (i>=2):
        print(i)
        i = i - 2
    else:
        print("Thank you for using this program")