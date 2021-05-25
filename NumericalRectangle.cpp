/*  1 1 1 1 1
    2 2 2 2 2
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5
*/

#include<iostream>
using namespace std;
int main()
{
    int n,i,j;

    cin>>n;

    if ( n>0 && n<=1000){
        for ( i=1 ; i<=n ; i++ ){
            for ( j=1 ; j<=n ; j++ )
            {
                cout<<i;
                if ( j<n ){
                    cout<<" ";
                }
            }
            cout<<endl;              

        }
    }
    return 0;
}