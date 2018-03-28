t=int(input())
for i in range(t):
    n=int(input())
    fact=1
    j=2
    while(j<=n):
        fact=fact*j
        j=j+1
    print(fact)