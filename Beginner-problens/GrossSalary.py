t=int(input())
for i in range(t):
    s=int(input())
    if(s<1500):
        print ( s + s*0.10 + s*0.90)
    else:
        print( s + 500 + s*0.98 ) 