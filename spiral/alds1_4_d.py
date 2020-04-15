# -*- coding : UTF-8 -*-

from collections import deque

n,k = map(int,input().split())
w = []
for _ in range(n):
    w.append(int(input()))

def v(P):
    # 最大荷重をPとしたときに、詰める荷物の総重量を求める関数
    # P >= max(w) の範囲でのみ考える

    track = {}
    num = 0

    for i in range(1,k+1):
        s = 0
        while s + w[num] <= P:
            s+=w[num]
            num+=1

            if num == n:
                return n

    return num

def solve():
    left = 0
    right = 100000 * 10000

    mid = (left+right)//2
    
    return P