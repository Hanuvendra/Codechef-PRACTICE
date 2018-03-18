t=int(input())
for j in range(t):
    a,b=map(int,input().split())
    lamik=0
    bob=0
    i=1
    while(1):
        lamik+=i
        bob=bob+i+1
        if(lamik>a):
            print("Bob")
            break
        if(bob>b):
            print("Limak")
            break
        i+=2
    j+=1
    
        