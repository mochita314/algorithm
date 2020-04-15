# -*- coding : UTF-8 -*-

n,k = map(int,input().split())
w = []
for _ in range(n):
    w.append(int(input()))

def merge(lst1,lst2):

    num1 = 0
    num2 = 0

    while num1<len(lst1) and num2<len(lst2):

        if lst1[num1] >= lst2[num2]:
            n = lst1[num1]
            lst.append(n)
            num1+=1
        else:
            n = lst2[num2]
            lst.append(n)
            num2+=1

    if num1 == len(lst1):
        lst.append(lst2[num2:])
    else:
        lst.append(lst1[num1:])
    
    return lst

def merge_sort(lst):

    if len(lst)<=1:
        return lst

    else:
        mid = len(lst)//2

        left = lst[:mid]
        right = lst[mid:]

        left = merge_sort(left)
        right = merge_sort(right)
    
    return merge(left,right)

w = merge_sort(w)

def solve(w):

    track = {}
    for i in range(1,k+1):
        track[i] = w[i-1]
    
    w = w[k:]

    t_num = k
    w_num = 0
    max_value = track[1]

    while w_num < n-k:    

        if track[t_num] + w[w_num] <= max_value:
            track[t_num] += w[w_num]
            w_num += 1

        elif t_num > 0:
            t_num -=1
        else:
            track[1]
        
        

         





    return 0