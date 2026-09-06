# write a python program which will accept the age of citizen and decide whether he is eligable to voteor not.


while(True):
    age = int(input("Enter age: "))
    if age >= 18:
        print("{} years old  you are eligible to vote".format(age))
        break
    else:
        print("{} years old  you are not eligible to vote".format(age))
