t=int(input())
for i in range(t):
    count=0
    count1=0
    l=int(input())
    a=[int(i) for i in input().split()]
    b=[int(j) for j in input().split()]
    c=b[::-1]
    for k in range(l):
        if(b[k]>=a[k]):
            count+=1
        if(c[k]>=a[k]):
            count1+=1
    if(count==l and count1==l):
        print("both")
    elif(count1==l):
        print("back")
    elif(count==l):
        print("front")
    else:
        print("none")
    i+=1
    
