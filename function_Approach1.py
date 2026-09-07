# sum of Two number
# ApproCH 1
"""
input = Taken from function call
process = done in function body
output = display in function call
"""
def addop(k,v):
    c = k+v
    return c
#main program
a = float(input("enter a number: "))
b = float(input("enter another number: "))
r = addop(a,b)
print("sum({},{}= {}".format(a,b,r))
