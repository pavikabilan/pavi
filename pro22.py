#pavithra
n=input()
n=int(n)
l=[]
for i in range(0,n):  
    n1=input()
    l.append(n1)
W=[]
for i in zip(*l):
    if i.count(i[0])==len(i): 
        W.append(i[0])
    else:
        break
print(''.join(W))
