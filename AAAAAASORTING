'''acending order '''
n=int(input("enter the range: "))
a=[]
for i in range (1,n+1):
    b=int(input("enter the value in list: "))
    a.append(b)
print("original list is: " ,a)
a.sort()
print("sorted list is: " ,a)



'''descending order'''
n=int(input("enter the range: "))
a=[]
for i in range (1,n+1):
    b=int(input("enter the value in list: "))
    a.append(b)
print("original list is: " ,a)
a.sort(reverse=True)
print("sorted list is: " ,a)


'''binary search'''
def binary_search(n,x):
    start=0
    end=len(n)-1
    found=False
    while(start <= end and not found):
        mid=(start+end)//2
        if n[mid] == x:
            found=True
        else:
            if n[mid]>x:
                end=mid-1
            else:
                start=mid+1
    return found
    
    
print(binary_search([1,2,3,4,5,6,7,8,9,9] , 9))



'''source code binary search'''
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))
    
    
