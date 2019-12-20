# Fance Repair 

import heapq

N=int(input())
L=[int(i) for i in input().split()]

fance=[]
heapq.heapify(fance)

for i in range(N):
    heapq.heappush(fance,L[i])
ans=0
while len(fance)>1:
    l1=heapq.heappop(fance)
    l2=heapq.heappop(fance)

    ans+=l1+l2
    heapq.heappush(fance,l1+l2)

print(ans)