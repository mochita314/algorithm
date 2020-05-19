from collections import deque

N=int(input())
A=list(map(int,input().split()))

def func(lst1,lst2):
    lst3=deque()
    for i in range(len(lst1)):
        lst3.append(lst1[i]-lst2[i])
    lst3 = list(lst3)
    lst3.sort()

    num=0
    for s in lst3:
        if s>0:
            break
        elif s==0:
            num+=1

    return num

ans=0
for i in reversed(list(range(0,N))):
    lst=deque()
    for j in list(range(0,i)):
        lst.append(i-j-A[i])
    B=deque(A[:i])
    ans += func(B,lst)

print(ans)