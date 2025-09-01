def second(l):
    l=list(set(l))
    l.sort()
    return l[-2]
print(second([1,2,3,4,5]))
