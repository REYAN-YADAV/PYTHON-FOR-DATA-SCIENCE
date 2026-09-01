# write a python program which accept a word and find it is palindrome or not>

word = input("enter word: ")
pal = "palindrome" if word.lower() == word[::-1].lower() else "not palindrome"
print("'{}' is {}".format(word,pal))
