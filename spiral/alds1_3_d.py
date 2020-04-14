from collections import deque

line = input()

s1 = deque()
s2 = deque()

n = len(line)
area = 0

for i in range(n):
    if line[i] == "\":
        s1.append(i)
    elif line[i] == "/":
        if s1: # if s1 is not empty
            dis = i - s1.pop()
            area += dis
        


