n=list(map(int,input().split()))
result=[]
zeros=0
for i in n:
    if i==0:
        zeros+=1
    else:
        result.append(i)
for i in range(zeros):
    result.append(0)
print(result)