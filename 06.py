menu=input().split()
p=list(map(int,input().split()))
order=input().split()
total=0
for i in range(len(menu)):
    a=menu[i]
    quantity=order.count(a)
    if quantity>0:
        total+=quantity*p[i]
        print(a,"X",quantity,"=",quantity*p[i])
print('Total:',total)