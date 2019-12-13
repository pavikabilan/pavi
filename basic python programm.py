#basic program
a=9
b=3
print(a+b)#add
print(a-b)#sub
print(a*b)#multiplication
print(a/b)#division quotient in float
print(a//b)#floor division print the quotient integer
print(a%b)#modulo operation show remainder alone 






#basic add program using loop
n=int(input())
sum=0
while(n>0): #check whether n is greater than 0 or not:
	sum+=n   #sum = sum + n ( add previous sum and next n)
	n-=1 # decrement n by 1
print(sum) # print the final sum

#basic add using for loop
sum=0
for i in range(1,10):   #  execute from 1 to 9
	sum+=i # sum=sum+i 
print(sum) #print the final sum 

	


