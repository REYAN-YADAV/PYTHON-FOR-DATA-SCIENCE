# write python program which will accwpt 3 numberical value find the bigger amongs them and  check for equality

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))

res = a if (a>=b) and (a>c) else b if (b>a) and (b>=c) else c if (c>=a) and (c>b) else "All values are equal"
print("Big({},{},{}) = {}".format(a,b,c,res))