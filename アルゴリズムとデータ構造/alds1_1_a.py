N=int(input())
lst=list(map(int,input().split()))
print(' '.join(map(str,lst)))

for i in range(1,len(lst)):
    j = i-1
    ele = lst[i]
    while j>=0 and lst[j] > ele:
        lst[j+1] = lst[j]
        j-=1
    lst[j+1] = ele
    print(' '.join(map(str,lst)))
        