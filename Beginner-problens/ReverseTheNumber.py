t=int(input())
for i in range(t):
    n=int(input())
    rev=0
    while(n>0):
        temp=n%10
        rev=rev*10 + temp
        n=n//10
    print(rev)