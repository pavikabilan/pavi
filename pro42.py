# pavithra
a5,b5=map(int,input().split())
if a5<=b5:
  d=a5
else:
  d=b5
z=[]
for i in range(0,d):
  z.append(sorted(list(map(int,input().split()))))
z=sorted(z)
for i in range(0,len(z[0])):
  for j in range(0,len(z)-1):
    if z[j][i]>z[j+1][i]:
      z[j][i],z[j+1][i]=z[j+1][i],z[j][i]
for i in z:
  print(*i)
