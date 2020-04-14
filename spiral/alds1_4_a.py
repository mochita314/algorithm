ns = int(input())
S = list(map(int,input().split()))
nt = int(input())
T = list(map(int,input().split()))

def linear_search(lst,key):
    i = 0
    while i<len(lst):
        if lst[i] == key:
            return 1
        else:
            i+=1
    return 0

ans = 0
for key in T:
    ans += linear_search(S,key)
print(ans)