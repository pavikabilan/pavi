#reverse the number

a=int(input("enter the number:"))
d=0
while a>0:
    rev=a%10
    d=(d*10)+rev
    a=a//10
print(d)


# sum of digits

a=int(input("enter the number:"))
sum=0
while a>0:
    d=a%10
    sum+=d
    a=a//10
print(sum)    

