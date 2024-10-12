#creating two list and user enter data in both and then extract even numbers from that 
n=[];m=[];o=[];p=[]
a = int(input("Enter the number of element in list 1: "))
b = int(input("Enter the number of element in list 2: "))
print('Enter data in lpist 1:')
for i in range(a):
    x=int(input())
    n.append(x)
print(n)
print('Enter data in lpist 2:')
for i in range(b):
    x=int(input())
    m.append(x)
print(m)
# marge two lists
for g in range(a):
    c=n[g]
    o.append(c)
for e in range(b):
    d=m[e]
    o.append(d)
print(o)
# extracting even numbers
for i in range(a+b):
    x=o[i]
    if x%2 == 0:
     p.append(x)
print(p)    
