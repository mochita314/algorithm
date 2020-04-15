A = int(input())
lst = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

"""
このコードだとタイムアウトになる

dp = [[-1 for j in range(2001)] for i in range(21)]

def func(i,j):
    # i番目以降の数の中から、和がjとなるように数を選ぶ

    if dp[i][j]!=-1:
        return dp[i][j]
    elif j==0:
        dp[i][j] = 1
        return 1
    elif i>=len(lst):
        dp[i][j] = 0
        return 0
    else:
        if lst[i]<=j:
            # i番目の数を使う
            ans = max(func(i+1,j-lst[i]),func(i+1,j))
        else:
            # i番目の数を使わない
            ans = func(i+1,j)

        return ans

for m_i in m:
    ans = func(0,m_i)
    if ans==1:
        print("yes")
    else:
        print("no")

"""