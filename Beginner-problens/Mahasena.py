t=int(input())
a=[int(i) for i in input().split()]
even=0
odd=0
for j in range(t):
    if(a[j]%2==0):
        even+=1
    else:
        odd+=1
if(even>odd):
    print("READY FOR BATTLE")
else:
    print("NOT READY")