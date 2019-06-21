
def sortInsert(L):
    res = [0]*len(L)
    for i in range(len(L)):
        v = L[i]
        for j in range(i):
            if(res[j]>v):
                tmp = res[j]
                res[j] = v
                v=tmp
        res[i]=v
    return res
                
L0=[1,2,3,4]
assert(L0==sortInsert(L0))
L=[4,3,2,1]
assert(L0==sortInsert(L))
L=[4,3,1,2]
assert(L0==sortInsert(L))

