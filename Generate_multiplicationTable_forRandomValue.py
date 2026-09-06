# write a python program which will generate multiplication Table for random numbers.
#          and read the list of random number from keyword

lst = list()
print("Enter list of Random values and press # to stop")
while (True):
    num = input()
    if (num != '#'):
        lst.append(int(num))
    else:
        break
for i in lst:

    if (i <= 0):
        print("{} invalid input".format(i))
    else:
        print("multiplication of {}".format(i))
        print("_" * 50)
        for j in range(1, 11):
            print("\t\t{} x {} = {}".format(i, j, i * j))
        else:
            print("_" * 50)
else:
    print("_" * 50)

