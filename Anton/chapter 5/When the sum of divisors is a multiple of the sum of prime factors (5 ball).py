def expandedForm(a):
    h=len(str(a))-1
    j=''
    l=str(a)
    for i in l:
        l = l[1::]
        if len(l)==0:
            j += i + "0" * h
            continue
        if i=="0":
            h-=1
            continue
        j+=i+"0"*h+" + "
        h-=1
    return j
print(expandedForm(12))
print(expandedForm(42))
print(expandedForm(70304))
print(expandedForm(5318514513))
