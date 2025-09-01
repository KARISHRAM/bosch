s="hello"
v="aeiouAEIOU"
vc=cc=0
for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1
print(vc,cc)
