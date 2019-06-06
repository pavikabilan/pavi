#pavi
from itertools import permutations
values=list(permutations(['d','h','o','n','i']))
x=input()
m=[]
for i in values:
  if i not in m:
    m.append(''.join(i))
for i in m:
  if i==x:
    print('yes')
    break
else:
  print('no')
