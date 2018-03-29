t=int(input())
for i in range(t):
    q,p=map(int, input().split())
    if(q<=1000):
        print(format( q*p,'.6f'))
    else:
        d=q*p*0.10
        print(format(q*p-d, '0.6f'))