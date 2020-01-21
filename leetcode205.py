def isIsomorphic1(s, t):
    d1,d2 = {},{}
    for i,val in enumerate(s):
        d1[val] = d1.get(val,[]) + [i]
    for i,val in enumerate(t):
        d2[val] = d2.get(val,[]) + [i]
    return sorted(d1.values()) == sorted(d2.values())


res = isIsomorphic1("egg","bar")
print(res)