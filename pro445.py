#pavi
no=input()
if no==no[::-1]:
    print("yes")
else:
    value=no.strip("0")
    
    if value==value[::-1]:
        print("yes")
    else:
        value=no.lstrip("0")
        
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
