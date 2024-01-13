#include<iostream>
using namespace std;
int main()
{
        int i,j,k,l,n,n1,n2; 
        l=0;k=0;
        cout<<"Enter a number: ";
        cin>>n;
        char ar[n*2][n*2];
        n2=n*2;
        n1=n*2;
        int temp=n;
        int row=0;
        int len = sizeof(ar)/sizeof(ar[0]);
        while(l<=n1 && k<=n2)
        {   
            for(i = l;i <= n2-1;i++)
            {   if(row%2==0){
                    ar[k][i]='*';
                }
                else{
                    ar[k][i]=' ';
                }
            }
            k++;
            for(i = k;i<=n1-1;i++)
            {   
                if(row%2==0){
                    ar[i][n2-1]='*';
                }
                else{
                    ar[i][n2-1]=' ';
                }
            }
            n2--;
            if (k<n1)
            {
                for (i = n2 - 1; i >= l; --i) 
                {
                    if(row%2==0){
                        ar[n1-1][i]='*';
                    }
                    else{
                        ar[n1-1][i]=' ';
                    }
                }
                n1--;
            }
            if (l < n2)
            {
                for (i = n1 - 1; i > k; --i) 
                {   
                    if(row%2==0){
                        ar[i][l]='*';
                    }
                    else{
                        ar[i][l]=' ';
                    }
                }
                if(row%2==0){
                    ar[i][l]=' ';
                }
                else{
                    ar[i][l]='*';
                }
                l++;
            }
            n--;
            row++;
        }
        if(temp%2==0){
            ar[temp-1][temp-1]=' ';
            }
        else{
            ar[temp-1][temp-1]='*';
        }    
        ar[temp][temp-1]=' ';
        for(i = 0; i <= len-1; i++)
        {
            for(j = 0; j <= len-1; j++)
            {
                cout<<ar[i][j]<<' ';
            }
            cout<<endl;
        }
    return 0;
}