n=int(input("enter number"))
i=2
sum=0
while i<=n:
    sum=sum+i
    if i<=(n-1):
        print(i,end=",")
    else:
        print(i,end="=")
   
    i=i+2
print(sum)