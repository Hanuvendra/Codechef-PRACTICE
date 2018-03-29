t=int(input())
for i in range(t):
    n=int(input())
    b=[int(i) for i in input().split()]
    c=[]
    for j in range(n):
        k=j+1
        while k<(n):
            sum=b[j]+b[k]
            c.append(sum)
            k+=1
    c.sort()
    print(c[0])