# while loop in while loop

i=1
print("While loop in while loop")
while (i<=4):
    print("_"*50)
    print("outer loop = {}".format(i))
    j=1
    while (j<=3):
        print("\t\t\tInner loop = {}".format(j))
        j = j+1
    else:
        i = i + 1
        print("_"*50)
else:
    print("_"*50)
