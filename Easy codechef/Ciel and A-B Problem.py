a,b=map(int , input().split())
n=a-b
if(n%10==9):
    print(n-1)
else:
    print(n+1)