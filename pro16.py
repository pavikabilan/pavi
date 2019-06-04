n1=int(input())
z=list(map(int,input().split()))
c=0
for i in range(len(z)):
    for j in range(i+1,len(z)):
        for k in range(j+1,len(z)):
            if z[i]<z[j]<z[k] and i<j<k:
                c=c+1
print(c)
