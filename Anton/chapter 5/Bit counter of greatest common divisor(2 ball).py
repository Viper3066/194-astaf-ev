def f(a):
    if a == []:
        return []
    if len(a) == 1:
        return a
    while True:
        if len(a) == 1 or a==[]:
            return []
        if a[0]+a[-1]==sum(a)-a[0]-a[-1]:
            return a
        else:
            a.remove(a[0])
            a.remove(a[-1])

print(f([1,2,3,4,5]))
print(f([0,104,3,101,0,111]))
print(f([1,-1]))
print(f([0]))
print(f([100,0,-100]))
print(f([4,4]))