t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    list=[a,b,c]
    list.sort()
    print(list[1])