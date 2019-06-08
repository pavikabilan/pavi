#pavithra
p,q = map(int,input().split())
q = q%p
r = list(map(int,input().split()))
s = r[-q:] + r[:-q]
print(*s)
