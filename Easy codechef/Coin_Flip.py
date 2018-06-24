t=int(input())
for i in range(t):
    g=int(input())
    for j in range(g):
        m,n,q=map(int,input().split())
        if(n%2==0):
            print(n//2)
        else:
            if(m==1):
                if(q==1):
                    print(n//2)
                else:
                    print(n//2 + 1)
            else:
                if(q==1):
                    print(n//2 + 1)
                else:
                    print(n//2)
        
    