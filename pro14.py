#pavithra
s,t=map(str,input().split())
l1=0
if len(s)>len(t):
  s,t=t,s
i=0
while i<len(s):
  l1+=(ord(t[i])-ord(s[i]))
  i+=1
for i in range(i,len(t)):
  l1+=ord(t[i])-ord('a')+1
print(l1)
