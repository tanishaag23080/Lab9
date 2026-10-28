s=input()
w=s.split()
words=[]
for i in w:
    if len(i)>3:
        words.append(i)
print(words)