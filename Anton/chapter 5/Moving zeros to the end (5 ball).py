def move_zeros(lst):
    s=lst.count(0)
    h=[]
    for i in lst:
        if i==0:
            continue
        h.append(i)
    for i in range(s):
        h.append(0)
    return h

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))