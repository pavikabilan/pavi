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

        
