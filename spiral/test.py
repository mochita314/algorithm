from collections import deque

lst1 = deque([8,5,1])
lst2 = deque([7,6,4,3,2])

num1 = 0
num2 = 0

lst = deque()
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
    while num2<len(lst2):
        lst.append(lst2[num2])
        num2+=1
else:
    while num1<len(lst1):
        lst.append(lst1[num1])
        num1+=1
print(lst)
    