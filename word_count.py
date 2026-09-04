#write a python program which will accept line of text and find number of words in given line of text?

words = input("Enter your sentence: ")
wordsplit = words.split()
print("_"*50)
print("Given words : {}".format(wordsplit))
print("Number of words {}".format(len(wordsplit)))
