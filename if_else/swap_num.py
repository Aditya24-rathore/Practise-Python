# WAP to swap two num without using third variable
a=int(input("enter first number"))
b=int(input("enter first number"))
print(a,b)
a,b=b,a
print(a,b)

# WAP to swap two num without using third variable
a=int(input("enter first number"))
b=int(input("enter first number"))
c=a
a=b
b=c
print(a,b)

# WAP to swap two num with using addition and subtraction
a=int(input("enter first number"))
b=int(input("enter first number"))
sum=a+b
a=sum-a
b=sum-b
print(a,b)