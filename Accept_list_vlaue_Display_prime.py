# Write a python program which will accept the list of values and display only prime.

print("Enter all the values you want to check if it is prime or not and stop by using #")
lst = list()
while (True):
    num = input()
    if (num != '#'):
        lst.append(int(num))
    else:
        break
prime_lst = list()
for i in lst:
    if i > 1:
        for j in range(2, (i + 2) // 2):
            if (i % j == 0):
                break
            else:
                pass
        else:
            prime_lst.append(i)
    else:
        pass
else:
    print("All prime numbers are = {}".format(prime_lst))






