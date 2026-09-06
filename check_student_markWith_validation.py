# ckeck student pass or not

# validation of student number
while(True):
    sno = input("Enter your student number : ")
    if sno.isdigit():
        if int(sno)>0:
            break
        else:
            print("{} invalid input for student number -try again".format(sno))
    else:
        print("{} invalid input for student number -try again".format(sno))
# validation of student name
while (True):
    sname = input("Enter your student name : ")
    if sname.isalpha():
        break
    else:
        print("{} invalid input for student name -try again".format(sname))
# validation for c-lang marks
while(True):
    clm = input("Enter your c-lang marks : ")
    if clm.isdigit():
        cm = int(clm)
        if (cm>=0 and cm<=100):
            break
        else:
            print("{} invalid input for student mark -try again".format(clm))
    else:
        print("{} invalid input for c-lang mark -try again".format(clm))

# validation for c++ lang marks
while(True):
    cpplm = input("Enter your c++ lang marks : ")
    if cpplm.isdigit():
        cppm = int(cpplm)
        if (cppm>=0 and cppm<=100):
            break
        else:
            print("{} invalid input for student mark -try again".format(cpplm))
    else:
        print("{} invalid input for cpp lang mark -try again".format(cpplm))

# validation of python marks
while(True):
    pylm = input("Enter your c-lang marks : ")
    if pylm.isdigit():
        pym = int(pylm)
        if (pym>=0 and pym<=100):
            break
        else:
            print("{} invalid input for student mark -try again".format(pylm))
    else:
        print("{} invalid input for c-lang mark -try again".format(pylm))

print(sno,sname,cm,cppm,pym)

# calculate total marks
total_mark = cm+cppm+pym
percent = round((total_mark/300)*100,2)
if (cm<40) or (cppm<40) or (pym<40):
    grade = "Fail"
else:
    if (250<=total_mark<=300):
        grade = "Distinction"
    elif (200<=total_mark<=249):
        grade = "First"
    elif (150<=total_mark<=199):
        grade = "Second"
    elif (120<=total_mark<=149):
        grade = "Third"
#Display Student marks report
print("_"*50)
print("\t\tStudent Mark Report")
print("_"*50)
print("\t\tStudent number : ",sno)
print("\t\tStudent name : ",sname)
print("\t\tStudent c lang mark : ",cm)
print("\t\tStudent c++ lang mark : ",cppm)
print("\t\tStudent python lang mark : ",pym)
print("_"*50)
print("\t\tTotal Mark : ",total_mark)
print("\t\tpercent : ",percent)
print("\t\tgrade : ",grade)

















