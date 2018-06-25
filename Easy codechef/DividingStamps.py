n=int(input())
l=list(map(int,input().split()))
i=1
sum1=0
sum2=0
while i<=n:
    sum1=sum1+i
    sum2=sum2+l[i-1]
    i=i+1
if(sum1==sum2):
    print ("YES")
else:
    print("NO")