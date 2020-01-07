# prime numbers


class Prime:
    def prime_num(self):
        self.n=int(input("enter the number:"))
        self.a=[]
        self.b=[]
        for self.i in range(self.n):
            self.a.append(self.i)
        print(self.a , end = " " )
        for self.j in self.a:
            if self.j>1:
                for self.k in (2,self.n):
                    if (self.j % self.k) == 0:
                        break
                else:
                    self.b.append(self.j)
        print(" \n prime numbers are:" ,self.b)
    
                
obj=Prime()
obj.prime_num()


#evenodd

class EvenOdd:
    def even_odd(self):
        self.n=int(input("enter the value of 'n': "))
        evenlist=[]
        oddlist=[]
        self.a=[]
        for self.i in range (self.n):
            self.a.append(self.i)
        print(self.a)
        for self.b in self.a:
            if self.b % 2 == 0:
                evenlist.append(self.b)
            else:
                 oddlist.append(self.b)
        print(" \n even list is", evenlist, end=" ")        
        print(" \n odd list is" , oddlist, end=" ")
obj=EvenOdd()
obj.even_odd()

        
