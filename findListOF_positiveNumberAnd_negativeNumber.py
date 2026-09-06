# write a python program which will accept list of numerical value and find list of +ve number and neagative number?
n = int (input("Enter how many values you have: "))
if n<= 0:
    print("enter a positive number")
else:
    poslst = []
    neglst = []
    for i in range(1,n+1):
        val = float(input("Enter your value :"))
        if val>0:
            poslst.append(val)
        else:
            neglst.append(val)
    else:
        print("positive list {}:".format(poslst))
        print("negative list {}:".format(neglst))
