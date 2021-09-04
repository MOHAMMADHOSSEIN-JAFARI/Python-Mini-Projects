a= []
b= int(input())
a.append(b)
while b != -1:
    b= int(input())
    a.append(b)
c= sorted(a)
print(c[-1])    
### or 
# a= []
# b= int(input())
# a.append(b)
# while b != -1:
#    b= int(input())
#     a.append(b)
# c = max(a)
# print(c)