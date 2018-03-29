t=int(input())
for i in range(t):
    n=int(input())
    count=0
    j=2
    while j<n//2:
        if(n%j==0):
            count+=1
            break
        j+=1
    if(count==0):
        print("yes")
    else:
        print("no")