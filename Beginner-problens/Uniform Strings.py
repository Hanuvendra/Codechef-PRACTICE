t=int(input())
for i in range(t):
    count=0 
    s=input()
    j=0
    while j< (len(s)-1):
        if((s[j]=='0' and s[j+1]=='1') or (s[j]=='1' and s[j+1]=='0')):
           count+=1
        j+=1
    if((s[0]=='0' and s[7]=='1') or (s[0]=='1' and s[7]=='0')):
           count+=1
    if((count==0) or (count==2)):
       print("uniform")
    else:
       print("non-uniform")
    i=i+1
       

           
