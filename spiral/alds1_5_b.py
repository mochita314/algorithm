# -*- coding : UTF-8 -*- 

n = int(input())
S = list(map(int,input().split()))

# 番兵を使ったやり方がよくわかっていない

global cnt
cnt = 0

def merge(left,right):

    merged = []
    l_num = 0
    r_num = 0

    while l_num<len(left) and r_num<len(right):

        global cnt
        cnt += 1

        if left[l_num] <= right[r_num]:
            merged.append(left[l_num])
            l_num += 1
        else:
            merged.append(right[r_num])
            r_num += 1

    if l_num == len(left):
        merged.extend(right[r_num:])
        cnt += len(right[r_num:])
    if r_num == len(right):
        merged.extend(left[l_num:])
        cnt += len(left[l_num:])
    
    return merged

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = (len(lst))//2

    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left,right)

print(' '.join(map(str,merge_sort(S))))
print(cnt)