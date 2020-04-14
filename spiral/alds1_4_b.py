n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

def binary_search(lst,key):
    left = 0
    right = len(lst)
    while left<right:
        mid = (left+right)//2
        if lst[mid]==key:
            return 1
        elif key < lst[mid]:
            right = mid
        else:
            left = mid+1
    return 0

ans = 0
for key in T:
    ans+=binary_search(S,key)
print(ans)