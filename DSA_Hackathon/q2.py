def rotateleft(d,a):
    for i in range(d):
        x=a.pop(0)
        a.append(x)
    return a

print(rotateleft(2,[1,2,3,4,5]))
