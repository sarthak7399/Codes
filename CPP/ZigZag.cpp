/*
1     2     3     4
5     6     7     8
9    10    11    12
13    14    15    16
17    18    19    20

1
5 2
9 6 3
13 10 7 4
17 14 11 8
18 15 12
19 16
20
*/
#include<iostream>
using namespace std;
int main(){
    int m,n;
    cout<<"Enter no. of rows:";
    cin>>m;
    cout<<"Enter no. of columns:";
    cin>>n;
    int ar[m][n];
    int prow=m+n-1;
    int k=0;
    cout<<"Enter the elements of the array:\n";
    for(int x=0;x<m;x++){
        for(int y=0;y<n;y++){
            cin>>ar[x][y];
        }
    }
    while(k<prow){
        for(int x=0;x<m;x++){
            for(int y=0;y<n;y++){
                if(x+y==k){
                    if(k<prow/2 || m==n){
                        cout<<ar[y][x]<<" ";
                    }
                    else if(m>n){    
                        cout<<ar[y+1][x-1]<<" ";
                    }
                    else{
                        cout<<ar[y-1][x+1]<<" ";
                    }
                }
            }
        }
        cout<<endl;
        k++;
    }
    return 0;
}