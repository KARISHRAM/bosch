def isbalanced(s):
    s1=[]
    d={')':'(',']':'[','}':'{'}
    for c in s:
        if c in '([{':
            s1.append(c)
        elif c in ')]}':
            if not s1 or s1[-1]!=d[c]:
                return'NO'
            s1.pop()
    return'YES'if not s1 else'NO'
    
print(isbalanced("{[()]}"))
print(isbalanced("{[(])}"))
print(isbalanced("{{[[(())]]}}"))
