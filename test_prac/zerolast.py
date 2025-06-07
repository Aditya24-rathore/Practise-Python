l=[10,0,20,0,9,0]
l1=[]
for i in l:
    if i!=0:
        l1.append(i)
n=len(l)-len(l1)
for i in range(n):
    l1.append(0)
print(l1)