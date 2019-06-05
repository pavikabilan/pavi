#ppp
ipt=int(input())
b=list(map(int,input().split()))
c=[]
m=1
for i in b:
  if i not in c:
    c.append(i)
for i in range(0,len(c)-1):
  if c[i]<c[i+1]:
    m+=1
print(m)
