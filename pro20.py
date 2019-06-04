#pavi
a=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,a):
    for j in range(0,i):
        if l[j]<l[i]:
            c=c+l[j]
print(c)  
