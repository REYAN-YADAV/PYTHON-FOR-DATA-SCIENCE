#write a python program which will accept line of text and find number of words  and its length and higest length in given line of text?

line = input("Enter any line of text : ")
noword = line.split()
d = {} #empty dict
for word in noword:
    d[word] = len(word)
else:

    dv = max(list(d.values()))
    lst = list()
    for k,v in d.items():
        if (v==dv):
            lst.append(k)
    else:
        print("Highest lenth words")
        for v in lst:
            print("\t\t{}".format(v))





