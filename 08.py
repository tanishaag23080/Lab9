s=input()
digit=[]
sum=0
for i in s:
    if i.isdigit():
        digit.append(int(i))
        sum+=int(i)
print(digit)
print("Sum:",sum)