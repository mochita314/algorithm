from collections import deque

stack = deque()

for i in input().split():
    if not i in ['+','-','*']:
        stack.append(int(i))
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        if i == "+":
            num = num1+num2
        elif i=="-":
            num = num2-num1
        else:
            num = num1*num2
        stack.append(num)

print(stack[0])

