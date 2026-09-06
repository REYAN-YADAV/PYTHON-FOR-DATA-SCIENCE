#for loop in for loop

for i in range(1,6):
    print("_"*50)
    print("\t Inner loop = {}".format(i)) # outer loop
    print("_"*50)
    for j in range(1,4):
        print("\t\t\t Outer loop = {}".format(j)) # inner loop
    else:
        print("----------------------------------------------------")
else:
    print("_____________________________________________________")


