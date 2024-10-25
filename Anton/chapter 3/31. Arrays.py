a=[1,2,3]
a_m=1
c=[]
for i in a:
    a_m*=i
for i in a:
    c.append(a_m//i)
print(c)