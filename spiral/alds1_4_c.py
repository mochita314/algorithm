mod = 4**12
T = {}

def str_to_int(str1):
    num = 0
    for i in range(len(str1)):
        s = str1[i]
        if s == "A":
            s = 1
        elif s == "T":
            s = 2
        elif s == "C":
            s = 3
        elif s == "G":
            s = 4
        num += (5**i)*s
    return num

def h1(key):
    return key%mod

def h2(key):
    return 1+key%(mod-1)

def h(key,i):
    return (h1(key)+i*h2(key))%mod

def insert(T,str1):
    i = 0
    num = str_to_int(str1)
    while True:
        key = h(num,i)
        if not key in T:
            T[key] = str1
            return 0
        else:
            i+=1

def search(T,str1):
    i=0
    num = str_to_int(str1)
    key = 0
    while True:
        key = h(num,i)
        if key not in T or key>=mod:
            print("no")
            return None
        elif T[key]==str1:
            print("yes")
            return key
        else:
            i+=1

n = int(input())
for i in range(n):
    command = input()
    if command[0] == "i":
        insert(T,command[7:])
    elif command[0] == "f":
        search(T,command[5:])