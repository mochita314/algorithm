N,W=map(int,input().split())
wv=[]
for _ in range(N):
    wv.append([int(i) for i in input().split()])

dp=[[-1 for i in range(W+1)] for j in range(N+1)]

def func(i,j):
    if dp[i][j]>-1:
        ans=dp[i][j]
    else:
        if i==N:
            ans=0
        elif wv[i][0]>j:
            ans=func(i+1,j)
        else:
            ans=max(func(i+1,j),func(i+1,j-wv[i][0])+wv[i][1])
        dp[i][j]=ans
    return ans

print(func(0,W))