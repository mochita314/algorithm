import heapq

N,L,P=map(int,input().split())
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]

gas=[]
heapq.heapify(gas)

A.append(L)
B.append(0)
N+=1

ans=0
pos=0
tank=P

for i in range(N):
    d=A[i]-pos
    while(tank-d<0):
        tank+=heapq.heappop(gas)*(-1)
        ans+=1
    tank-=d
    pos=A[i]
    heapq.heappush(gas,-B[i])

print(ans)


