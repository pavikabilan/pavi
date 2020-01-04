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




a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
for i in range(a,b):
    rev=0
    while(i>0):
        rem=i%10
        rev=(rev*10)+rem
        i=i//10
    print(rev) 
    
    
    
    
a=int(input("enter the number:"))
for i in range(1,a):
    sum=0
    while i>0:
        d=i%10
        sum+=d
        i=i//10
    print(sum)   
    
    
    
    
    
    a=int(input())
for i in range(1,a):
    fact=1
    while(i>0):
        fact=i*fact
        i-=1
    print(fact)

 
    

    #fibonacci
    
    
    def fibonacci(n):
    a=0
    b=1
    count=0
    if n==0:
        print('enter the positive value')
    elif n==1:
        print(a)
    else:
        while(count<n):
            print(a, end=' ')
            c=a+b 
            a=b 
            b=c 
            count+=1
            

fibonacci(10)            
        
    
    
    
    

    
    
    
