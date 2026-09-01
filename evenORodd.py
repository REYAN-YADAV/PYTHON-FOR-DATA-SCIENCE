# write a python program which accept any numberical value and decide even or odd

n = float(input("Enter a number: "))
res = "even" if (n % 2 == 0) else "odd"
print("{} is {}".format(n,res))