#write a python program which will accept line of text and find number of words  and its length in given line of text?

line = input("Enter any line of text : ")
noword = line.split()
d = {} #empty dict
for word in noword:
    d[word] = len(word)
else:
    print(d)
    for word,length in d.items():
        print("{} ---> {}".format(word,length))






