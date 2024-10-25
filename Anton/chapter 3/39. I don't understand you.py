import random
from time import perf_counter

i = 'Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.'
print(i)
words = i.split()
h = []
h1=[]
s = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')

for word in words:
    if word[0] in s and word[-1] in s:
        h.append(word)
    else:
        if word[0] in s or word[0] in s1:
            h.append(word[:-1])
            h.append(word[-1])
        elif word[-1] in s or word[-1] in s1:
            h.append(word[1:])
            h.append(word[0])
for i in h:
    if len(i)==1:
        h1.append(i)
        continue
    q=[]
    for i1 in i:
        q.append(i1)
    if (len(i)-2)==1 or len(i)-2==0:
        l=1
        l1=1
    else:
        l=random.randint(1,len(i)-2)
        l1 = random.randint(1, len(i) - 2)
    n=i[l]
    q[l]=q[l1]
    q[l1]=n
    h=''
    for i in q:
        h+=i
    h1.append(h)
z=''
for i2 in h1:
    if len (i2)==1 and not(i2 in s) :
        z+=i2
    else:
        z+=" "+i2
z=z.replace(" ",'',1)
print(z)

