t=int(input())
for i in range(t):
    n=input()
    b=[]
    for ch in n:
        b.append(ch)
    print(int(b[0]) + int(b[len(b)-1]))
                    