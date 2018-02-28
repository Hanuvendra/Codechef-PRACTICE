#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int A[20];
    int i,n,j;
    int count;
    cin>>n;
    for(j=0;j<n;j++)
    {
        count=0;
        for(i=0;i<5;i++)
        {
            cin>>A[i];
            if(A[i]==1)
              count++;
        }
        if(count==0)
          cout<<"Beginner"<<endl;
        else if(count==1)
          cout<<"Junior Developer"<<endl;
        else if(count==2)
          cout<<"Middle Developer"<<endl;
        else if(count==3)
          cout<<"Senior Developer"<<endl;
        else if(count==4)
          cout<<"Hacker"<<endl;
        else
          cout<<"Jeff Dean"<<endl;
     }
     return 0;
}
