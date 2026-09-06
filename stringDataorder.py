# write a python program which will impliment the following
"""
write a python program which will implement the following
given lie of test = sting47py1th2on6
cae11
Expected output : [string pytohn]
expected output : [426 71]
case2
Expected output : [psghinnony] ->Acending order
Expected output [642] ->decending order [17] -> decending order


"""
# validation of input string
while (True):
    line = input("Enter the line of text: ")
    if line.isalnum():
        break
    else:
        print("please enter only alphanumeric characters ")
        print("Try Again")

strlst = []
evenlst = []
oddlst = []
for char in line:
    if char.isalpha():
        strlst.append(char)
    elif char.isdigit():
        if (int(char)%2==0):
            evenlst.append(char)
        else:
            oddlst.append(char)

strlst.sort()
strline = ""
strline = strline.join(strlst)
print(strline)
evenlst.sort(reverse=True)
print(evenlst)
oddlst.sort(reverse=False)
print(oddlst)

































