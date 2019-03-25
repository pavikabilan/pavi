#pavithra
x=str(input())
def reversewordsentence(x):
    return ' '.join(word[::-1] for word in x.split(" "))
print(reversewordsentence(x)) 
