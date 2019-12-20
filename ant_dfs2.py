from collections import deque

N,M=map(int,input().split())

MAP=[]
for _ in range(N):
    MAP.append([str(s) for s in input()])

distance=[[-1 for i in range(M)] for j in range(N)]

q=deque()

for i in range(N):
    for j in range(M):
        if MAP[i][j]=="S":
            q.append((i,j))
            distance[i][j]=0
            break
    else:
        break

def bfs():
    while q:
        (x,y)=q.popleft()
        for nx,ny in[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if nx<0 or nx>=N or ny<0 or ny>=M or \
                MAP[nx][ny]=="#" or distance[nx][ny]>-1:
                continue
            else:
                distance[nx][ny]=distance[x][y]+1
            q.append((nx,ny))

            if MAP[nx][ny]=="G":
                print(distance[nx][ny])
                exit()
                
bfs()