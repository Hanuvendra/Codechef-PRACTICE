https://www.codechef.com/problems/INTESTa,b=map(int , input().split())
count=0
for i in range(a):
    c=int(input())
    if(c%b==0):
        count+=1
print(count)