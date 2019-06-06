#pavui
st=input()
flag3=0
for i in range(0,len(st)-1):
  for j in range(i+1,len(st)):
    if st[i]<st[j]:
      flag3=1
      print(st[j:])
      break
  if flag3==1:
    break
else:
  print(st)
