t=int(input())
for i in range(t):
    n=int(input())
    m=input()
    i=0
    y=0
    n=0
    for ch in m:
        if(ch=='I'):
            i+=1
        elif(ch=='Y'):
            y+=1
        elif(ch=='N'):
            n+=1
    if(y==0 and i==0):
        print("NOT SURE")
    elif(i==0):
        print("NOT INDIAN")
    elif(y==0):
        print("INDIAN")