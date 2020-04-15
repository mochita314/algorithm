# -*- coding : UTF-8 -*-

from collections import deque

n,k = map(int,input().split())
w = []
for _ in range(n):
    w.append(int(input()))

def merge(lst1,lst2):

    num1 = 0
    num2 = 0

    while num1<len(lst1) and num2<len(lst2):

        if lst1[num1] <= lst2[num2]:
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

w = deque(merge_sort(w)) # 昇順に並べなおし、dequeにする

def v(P):
    # 最大荷重をPとしたときに、詰める荷物の総重量を求める関数
    # P >= max(w) の範囲でのみ考える

    track = {}
    weight = 0

    for i in range(k):
        n = w.pop()
        track[i] = n
        weight += n

    # 荷物を小さい順に、大きい荷物が入ってるトラックから順に入れて行く
    num = k-1

    while num>=0:

        if num == k-1:
            n = w.popleft()

        if track[num] + n <= P:
            track[num] += n
            weight += n
            num = k-1
        else:
            num-=1
    
    return weight

sum(w)+1 = max_p

dp = [0 for i in range(w[n-1],max_p)]

for p in range(w[n-1],max_p):
    
    
