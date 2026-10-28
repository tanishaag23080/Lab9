s=input()
word=s.split()
result=[]
for i in word:
    result.append(i[::-1])
print(" ".join(result))