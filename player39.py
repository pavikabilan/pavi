#pavithra
x=int(input())
def ispoweroftwo(x):
    return(x and (not(x&(x-1))))
if(ispoweroftwo(x)):
    print("yes")
else:
    print("no")
