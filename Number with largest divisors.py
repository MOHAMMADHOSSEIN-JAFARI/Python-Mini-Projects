a= []
for i in range(1, 4):
    b = int(input())
    a.append(b)

c = []

for z in a:
    count= 0
    for w in range(1, z+1):
        if z % w == 0:
            count += 1
    c.append(count)    
m= max(c)
t= [s for s, j in enumerate(c) if j == m] #choosing the position of nemebr(s) with largest divisors 

u= []
for T in t:
    u.append(a[T])
mm= max(u)
print(mm,"", m)

    
    
    
