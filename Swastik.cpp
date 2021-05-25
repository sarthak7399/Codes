/*  *  ****
    *  *
    *  *
    *******
       *  *
       *  *
    ****  * 
*/

#include<iostream>
using namespace std;
int main()
{
    int n,i,j,mid;

    cout<<"Enter an odd number:";
    cin>>n;

    if ( n%2!=0 && n<100 && n>4)
    {
        mid=n/2;
        mid++;

        for ( i=1 ; i<=n ; i++ ){
            for ( j=1 ; j<=n ; j++ )
            {
                if ( i<mid ){
                    if ( j==1 || j==mid)
                    cout<<"*";
                    if ( j>mid && i==1 )
                    cout<<"*";
                    else if ( j>1 && j<mid)
                    cout<<" ";
                }
                if ( i==mid ){
                    cout<<"*";
                }
                if ( i>mid ){
                    if ( j==n || j==mid)
                    cout<<"*";
                    if ( j<mid && i==n )
                    cout<<"*";
                    else if ( (j>=1 && j<mid) || ((j>mid && j<=n)) )
                    cout<<" ";
                }
            }
            cout<<endl;
        }
    }
    return 0;
}