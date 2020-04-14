N = int(input())
lst = list(input().split())
lst2 = []
for i in lst:
    lst2.append(i)

def bubble_sort(lst):

    flag = 1
    while flag:
        flag = 0
        for i in reversed(list(range(1,len(lst)))):
            if int(lst[i-1][1])>int(lst[i][1]):
                lst[i-1],lst[i] = lst[i],lst[i-1]
                flag = 1

    return lst

def selection_sort(lst):


    for i in range(len(lst)):
        min_i = i
        for j in range(i+1,len(lst)):
            if int(lst[j][1]) < int(lst[min_i][1]):
                min_i = j
        lst[i],lst[min_i] = lst[min_i],lst[i]

    return lst

list1 = bubble_sort(lst)
list2 = selection_sort(lst2)

print(' '.join(map(str,list1)))
print("Stable")
print(' '.join(map(str,list2)))
if list1 == list2:
    print("Stable")
else:
    print("Not stable")

