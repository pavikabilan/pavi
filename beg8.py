#pavi
n=int(input())
if n<0:
    print("enter positive number")
else:
    s=0
    while n>0:
        s+=n
        n-=1
    print("s",s)    
