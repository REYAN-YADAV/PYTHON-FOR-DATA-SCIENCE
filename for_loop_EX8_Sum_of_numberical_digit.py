# Write a python program which will accept a numerical value and find sum of its digit?

num = input("Enter a number: ")
if num.isdigit():
    sum = 0
    for d in num:
        i = int(d)
        sum = sum + i
    else:
        print("sum of digit of {} is {}".format(num, sum))
else:
    print("please enter numerical value")



