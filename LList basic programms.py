#count no of even &odd in the list
list=[1,2,3,4,5,6,7,8,9,10,44,55,66,77,88,99,11,22,33,34,56,76]
evencount=0 
oddcount=0
for i in list:
    if i%2==0:
        evencount+=1
    else:
        oddcount+=1
print(evencount)
print(oddcount)

# split even & odd in list

def split(list):
    evenlist=[]
    oddlist=[]
    for i in list:
        if i%2==0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("even list=" ,evenlist)
    print("odd list=" ,oddlist)        

list=[]
n=int(input('enter the value:'))
for  j in range(0,n):
    x = int(input())
    list.append(x)
split(list)
