# write a python program which accept any word and decide whether it is a vowel or not.
word = input("Enter a word: ")
res = "vowel" if word.lower() in "aeiou" else "not vowel"
print("{} is {}".format(word,res))
