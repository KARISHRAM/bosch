def bs(l,x):
    low,high=0,len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
print(bs([1,2,3,4,5,6,7],4))
