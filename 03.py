ball=input().split()
total=0
Wic=0
B=0
over=[]
run=0
for i in range(len(ball)):
    a=ball[i]
    if a=='W':
        Wic+=1
    else:
        r=int(a)
        total+=r
        run+=r
        if r==4 or r==6:
            B+=1
    if (i+1)%6==0:
        over.append(run)
        run=0
if len(ball)%6!=0:
    over.append(run)
print('total runs:',total)
print('wicket:',Wic)
print('boundaries:',B)
print('runs per over:',over)