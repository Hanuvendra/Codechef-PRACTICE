t=int(input())
for i in range(t):
    a=input()
    b=input()
    a=''.join(set(a))
    mini=0
    for j in range(len(a)):
        mini=mini+b.count(a[j])
    print(mini)