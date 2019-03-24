#nikitha
str=str(input())
newstr= ''
for i in range(len(str)//2):
    newstr+=str[i*2+1]+str[i*2]
if len(str)%2!=0:
    newstr+=str[-1]
print(newstr)
