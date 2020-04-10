N,M=map(int,input().split())

W=[]
for i in range(N):
    W.append([])

for i in range(N):
    for c in input():
        W[i].append(c)

def dfs(x,y):
    W[x][y]='.'

    for dx in range(-1,2):
        for dy in range(-1,2):
            nx=x+dx
            ny=y+dy
            if nx>=0 and nx<N and ny>=0 and ny<M and W[nx][ny]=='W':
                dfs(nx,ny)

ans=0
for i in range(N):
    for j in range(M):
        if W[i][j]=='W':
            dfs(i,j)
            ans+=1

print(ans)
