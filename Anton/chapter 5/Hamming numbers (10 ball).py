def hamming(l):
    h1 = set()
    h = set()
    h.add(1)
    h1.add(1)
    for i in range(l):
        mini=min(h)
        h.remove(min(h))
        for i1 in [2,3,5]:
            n=i1*mini
            h.add(n)
            h1.add(n)
    h1=sorted(h1)
    return h1[l-1]


print(hamming(20))
print(hamming(5000))


