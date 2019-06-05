#pavithra
n=int(input())
l=list(map(int,input().split()))
m1=[]
for i in l:
	s=bin(i)[2::]
	m1.append(([s.count("1"),i]))
m1.sort(reverse=True)
for i in range(0,len(m1)):
	print(m1[i][1])
