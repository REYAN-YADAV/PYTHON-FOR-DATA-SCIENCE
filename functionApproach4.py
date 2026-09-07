# sum of Two number
# ApproCH 3
"""
input = Taken in function body
process = done in function body
output = display in function call
"""
def sum():
    #input
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    # process
    c = a + b
    return a,b,c
# main program
a,b,c = sum()
print("sum({},{} = {})".format(a,b,c))
print("_"*50)
res = sum()
print(res, type(res))
print("_"*50)
print("sum({},{} = {})".format(res[0],res[1],res[2]))
print("_"*50)