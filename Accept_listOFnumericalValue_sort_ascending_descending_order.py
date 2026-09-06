# write a python program for accepting list of numerical values and sort them in both  ascending and descending order?
lst = list()
print("Enter list of numerical values and press @ to stop inputing? ")
while (True):
    value = input()
    if value != "@":
        lst.append(float(value))
    else:
        break
print(lst)
asc = sorted(lst)
dec = sorted(lst,reverse=True)
print("Ascending order = ", asc)
print("Descending order =",dec)
