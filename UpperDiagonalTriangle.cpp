/*  12345
    1234    
    123
    12
    1
*/

#include<iostream>
using namespace std;
int main()
{
    int n,i,j;

    cout<<"Enter an odd number:";
    cin>>n;


        for ( i=1 ; i<=n ; i++ ){
            for ( j=1 ; j<=n+1-i ; j++ )
            {
                cout<<j;
            }
            cout<<endl;
        }
    return 0;
}