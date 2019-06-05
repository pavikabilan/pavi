#python
n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(len(a)):
    if(i%2==0):
        b.append(a[i])
    else:
        c.append(a[i])
for j in b:
    d=sum(b)
for k in c:
    f=sum(c)
if(d>f):
    print(d)
else:
    print(f)
