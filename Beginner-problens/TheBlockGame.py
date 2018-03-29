t=int(input())
for i in range(t):
    n=int(input())
    rev=0
    temp=n
    while(n>0):
        temp1=n%10
        rev=rev*10+temp1
        n=n//10
    if(temp==rev):
        print("wins")
    else:
        print("losses")