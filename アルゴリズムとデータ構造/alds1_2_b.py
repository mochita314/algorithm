N = int(input())
lst = list(map(int,input().split()))

swap=0
for i in range(len(lst)):
    min_i = i
    for j in range(i+1,len(lst)):
        if lst[j] < lst[min_i]:
            min_i = j
    lst[i],lst[min_i] = lst[min_i],lst[i]
    if lst[i]!=lst[min_i]:
        swap+=1

print(' '.join(map(str,lst)))
print(swap)