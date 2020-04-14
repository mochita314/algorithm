from collections import deque

line = input()

s1 = deque()
s2 = deque()

n = len(line)
total_area = 0

for i in range(n):
    if line[i] == "\\":
        s1.append(i)
    elif line[i] == "/":
        if s1: # if s1 is not empty
            j = s1.pop()
            area = i - j
            total_area += area
            if s2 and j < s2[-1][0]: # integrate the area of ponds
                while s2 and j < s2[-1][0]:
                    pre_pond = s2.pop()[1]
                    area += pre_pond
            s2.append([j,area])

print(total_area) 
if total_area!=0:
    print("{} ".format(len(s2)) + " ".join([str(x[1]) for x in s2]))
else:
    print(0)