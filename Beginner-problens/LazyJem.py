t=int(input())
for i in range(t):
    jeam=0
    n,b,m=map(int,input().split())
    while(n>0):
        if(n%2==0):
            n=int(n/2)
            jeam=jeam+n*m+b
            m=m*2
        else:
            n=int((n+1)/2)
            jeam=jeam+n*m+b
            m=m*2
            n=n-1
    print(jeam-b)
    i+=1
            