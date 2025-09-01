n=20
for i in range(2,n+1):
    f=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            f=False
            break
    if f:
        print(i,end=" ")
