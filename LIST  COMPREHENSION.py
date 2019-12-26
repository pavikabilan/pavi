x = [i for i in range(10,20)]
print(x)

y = [i for i in range(10,30) if i % 2 ==0]
print(y)

z = [i if i % 2 == 0 else "odd" for i in range(10,20)]
print(z)

a = {i:"value" for i in range(10,20)}
print(a)

b = {i: "Even" if i % 2 == 0 else "odd" for i in range(20,30)}
print(b)

c={i:"even" for i in range(10,50) if i%2==0}
print(c)
