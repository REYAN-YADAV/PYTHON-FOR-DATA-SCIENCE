# Write a python program which accept any numberical value and decide whether +ve,-ve,zero
n = float(input("Enter a number: "))
res = "positive" if (n > 0) else "negative" if (n < 0) else "zero"
print("{} is {}".format(n,res))
