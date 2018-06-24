t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    a=[]
    for j in range(m):
        if(l.count(j+1) == 0):
            a.append(j+1)
    b=[]
    c=[]
    for k in range(len(a)):
        if(k%2==0):
            b.append(a[k])
        else:
            c.append(a[k])
    if(len(b)==0):
        print(" ")
    else:
        print(*b,sep=' ')
    if(len(c)==0):
        print(" ")
    else:
        print(*c,sep=' ')
    