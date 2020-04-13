N=int(input())
lst=list(map(int,input().split()))

swap=0
while flag:
    flag = 0
    for i in reversed(list(range(1,len(lst)))):
        if lst[i-1]>lst[i]:
            lst[i-1],lst[i] = lst[i],lst[i-1]
            flag = 1
            swap+=1