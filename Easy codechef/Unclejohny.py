t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=int(input())
    a=l[m-1]
    l.sort()
    for j in range(n):
        if(l[j]==a):
            print(j+1)
            break