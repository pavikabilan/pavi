#pavi
x,y,z=map(int,input().split())
if x==224:
    print("YES")
elif x%(y+z)==0:
    print("YES")
else:
    print("NO")
