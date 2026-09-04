# Write a python program which will accept any word or line of text and display each and every character of a word or line of text?

n = input("Enter a any word:")
le = len(n)

i = 0
while (i < le):
    print(n[i])
    i = i + 1
else:
    print("No more words")

# Write a python program which will accept any word or line of text and display each and every character rd or line of text?

line = input("Enter a any word:")[::-1]
i = -len(line)
while (i <= -1):
    print(line[i])
    i = i+1
else:
    print("No more words")