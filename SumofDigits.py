for i in range(int(input())):
    n=input()
    b=[]
    for ch in n:
        b.append(ch)
    b=list(map(int,b))
    print(sum(b))