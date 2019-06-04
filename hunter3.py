#python
n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(0,n):
  if(a[i]==i):
    b.append(i)
c=set(b)
if(len(c)==0):
  print('-1')
else:
  print(*c)
