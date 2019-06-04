#pavithra
n = int(input())
a = list(map(int,input().split()))
b=[]
for i in range(0,len(a)):
  c=a.count(a[i])
  b.append(c)
for i in range(0,len(b)):
  if(b[i]==1):
    print(a[i])
