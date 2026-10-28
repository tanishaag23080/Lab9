n=int(input())
count={}
for i in range(n):
    a=input().split()
    first=a[0].lower()
    last=a[1].lower()
    name=first+"."+last
    if name not in count:
        count[name]=i
        email=name+"@jklu.edu.in"
    else:
        count[name]+=1
        email=name+str(count[name])+"@jklu.edu.in"
        
    print(email)