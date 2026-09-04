# write a pytohn program which will accept any value and find its reverse without slice operation
val = input("Enter any value : ")
rv = ""
for index in range(len(val)-1,-1,-1,):
    print("{} --> {}".format(index,val[index]))
    rv = rv + val[index]
else:
    print("\t\t{}".format(rv))
