t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    min=abs(l[0]-l[1])
    for j in range(n-1):
        if(abs(l[j]-l[j+1]) < min):
            min=abs(l[j]-l[j+1])
    print(min)