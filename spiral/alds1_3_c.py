from collections import deque

dll = deque()

n = int(input())
for _ in range(n):
    command = input()
    if command[0] == "i":
        dll.appendleft(command[7:])
    elif command[0] == "d":
        if command[6] == ' ':
            key = command[7:]
            if key in dll:
                dll.remove(key)
        elif command[6] == "F":
            dll.popleft()
        else:
            dll.pop()

print(' '.join(dll))