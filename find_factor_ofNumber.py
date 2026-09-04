# write a python program  which will accept any number and find its factor?
no = int(input("Enter the number which you want to find its factor of: "))
lst=list()
if no>0:
    for i in range(1, no // 2 + 1):
        if no % i == 0:
            print(i)
            lst.append(i)
    else:
        print(lst)
else:
    print("Please enter +ve number")

