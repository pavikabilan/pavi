#reverse the number

a=int(input("enter the number:"))
d=0
while a>0:
    rev=a%10
    d=(d*10)+rev
    a=a//10
print(d)    
