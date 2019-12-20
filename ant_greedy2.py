N=int(input())
L=[int(i) for i in input().split()]

def func1(L,N):
    ans=0
    while N>1:
        L.sort()
        ans+=L[0]+L[1]
        L[1]+=L[0]
        L.pop(0)
        N-=1
    return ans

print(func1(L,N))
"""
def func2(L):
    L.sort()
    ans=0
    for i in range(N):
        ans+=L[i]*(N-i)
    ans-=L[0]
    return ans

print(func2(L))
"""





