t=int(input())
for i in range(t):
    a=input()
    count=0
    for j in range(len(a)-2):
        b=a[j:j+3]
        if(b=="101" or b=="010"):
            count=count+1
            break
    if(count==1):
        print("Good")
    else:
        print("Bad")