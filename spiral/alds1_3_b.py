from collections import deque

N,Q = map(int,input().split())
deque_name = deque()
deque_time = deque()

for _ in range(N):
    a = list(input().split())
    deque_name.append(a[0])
    deque_time.append(int(a[1]))
v
now = 0
num=0
finished={}

while deque_name:

    name = deque_name.popleft()
    time = deque_time.popleft()

    if time<=Q:
        now+=time
        num+=1
        lst = [name,now]
        finished[num] = lst

    else:
        now+=Q
        time-=Q
        deque_name.append(name)
        deque_time.append(time)
    
for i in range(1,num+1):
    value = finished[i]
    print(' '.join(map(str,value)))
