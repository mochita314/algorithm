N=int(input())
S=input()
T=""

def func(a,b):
    global T
    while(a<=b):
        for i in range(b-a+1):
            if S[a+i]<S[b-i]:
                left=True
                break
            elif S[a+i]>=S[b-i]:
                left=False
                break
        if left:
            T+=S[a+i]
            a+=1
            print(T,"a")
        else:
            T+=S[b-i]
            b-=1
            print(T)
    return T

print(func(0,N-1))